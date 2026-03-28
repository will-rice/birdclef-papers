"""Fetch BirdCLEF-related papers from multiple sources.

Sources:
* **arXiv** – preprint server (cs, eess, q-bio categories).
* **Semantic Scholar** – broad coverage of journals, conferences, and
  additional preprint servers not indexed by arXiv.
* **DBLP** – bibliographic index covering CEUR-WS LifeCLEF / BirdCLEF
  workshop working-notes that are not posted to arXiv.
* **bioRxiv via Crossref** – ecology and bioacoustics preprints on bioRxiv.
* **Papers With Code** – community-curated ML papers, catches any gaps.

It is designed to be run in two modes:

* **Historical (first run)**: pulls everything submitted since the start of
  the LifeCLEF/BirdCLEF era (2016-01-01 onwards).
* **Incremental (scheduled)**: pulls only papers submitted in the last N days
  (default 8, so a weekly cron with a one-day overlap never misses anything).

Results are written to ``papers.csv`` in the repository root and the
``README.md`` table is regenerated from that file.

Usage::

    # Full historical fetch (first-run / back-fill):
    python scripts/fetch_papers.py --full

    # Incremental fetch (last 8 days, for weekly cron):
    python scripts/fetch_papers.py

    # Incremental fetch for the last N days:
    python scripts/fetch_papers.py --days 30
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
README_MD = REPO_ROOT / "README.md"

# ---------------------------------------------------------------------------
# arXiv
# ---------------------------------------------------------------------------

# arXiv API base URL (use https for TLS)
ARXIV_API_BASE = "https://export.arxiv.org/api/query"

# Search queries – cast a wide net over BirdCLEF and related topics.
ARXIV_SEARCH_QUERIES = [
    "BirdCLEF",
    "bird sound recognition",
    "bird call recognition",
    "bird song recognition",
    "bird species identification audio",
    "bird vocalization classification",
    "avian sound classification",
    "bioacoustics deep learning",
    "passive acoustic monitoring birds",
    "soundscape bird",
    "bird audio detection",
    "bird species classification spectrogram",
    "ecoacoustics machine learning",
    "bird call detection",
    "LifeCLEF bird",
    # Additional queries to find more relevant papers
    "BirdNET",
    "xeno-canto",
    "avian bioacoustics",
    "bird acoustic identification",
    "automated bird identification",
    "bird sound classification deep learning",
    "bird species acoustic",
    "soundscape ecology machine learning",
    "wildlife acoustic monitoring",
    "ornithology deep learning",
    "bird audio neural network",
    "avian call classification",
    "bird sound event detection",
    "bird sound dataset",
    "PAM birds",
    "bird species recognition neural",
    "mel spectrogram bird classification",
    # Techniques commonly used in BirdCLEF solutions
    "bird call transfer learning",
    "bioacoustics transfer learning",
    "bird sound self-supervised",
    "bird sound contrastive learning",
    "bird call few-shot",
    "bioacoustics few-shot learning",
    "bird species weakly supervised",
    "bird call pseudo label",
    "bird sound domain adaptation",
    "bird call transformer",
    "bird audio multi-label classification",
    # Specific models and tools
    "Perch bioacoustics",
    "BirdSet dataset",
    "AudioMoth bird",
    "bird sound EfficientNet",
    "bioacoustic foundation model",
    # Broader related areas
    "bird vocalization deep learning",
    "avian species recognition deep learning",
    "bird vocalization recognition",
    "nocturnal flight call detection",
    "bird species audio benchmark",
    "soundscape species identification",
    "biodiversity acoustic monitoring deep learning",
    "bird sound separation",
    "bird call identification neural",
    "avian sound detection",
]

# Keep old name as alias for backward-compat within this file.
SEARCH_QUERIES = ARXIV_SEARCH_QUERIES

# arXiv XML namespaces
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# ---------------------------------------------------------------------------
# Semantic Scholar
# ---------------------------------------------------------------------------

SS_BULK_API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
SS_FIELDS = (
    "paperId,title,authors,abstract,publicationDate,year,"
    "externalIds,openAccessPdf"
)

SS_SEARCH_QUERIES = [
    "BirdCLEF",
    "bird sound recognition",
    "bird vocalization classification",
    "avian bioacoustics deep learning",
    "passive acoustic monitoring birds",
    "LifeCLEF bird",
    "BirdNET bird identification",
    "bird call classification neural network",
    "bird species audio identification",
    "soundscape ecology bird machine learning",
    "ecoacoustics bird deep learning",
    "automated bird species recognition",
]

# ---------------------------------------------------------------------------
# DBLP (covers CEUR-WS LifeCLEF / BirdCLEF working notes)
# ---------------------------------------------------------------------------

DBLP_API_BASE = "https://dblp.org/search/publ/api"
DBLP_PAGE_SIZE = 100

DBLP_SEARCH_QUERIES = [
    "BirdCLEF",
    "LifeCLEF bird",
    "bird sound recognition CLEF",
    "avian sound classification CLEF",
    "bird species identification audio CLEF",
    "passive acoustic monitoring LifeCLEF",
]

# ---------------------------------------------------------------------------
# bioRxiv via Crossref
# ---------------------------------------------------------------------------

CROSSREF_API_BASE = "https://api.crossref.org/works"
CROSSREF_PAGE_SIZE = 100

# Polite-pool identifier sent with every Crossref request.
CROSSREF_MAILTO = "birdclef-papers@github.io"

# Only keep preprints whose DOI starts with this prefix (bioRxiv / medRxiv
# Cold Spring Harbor Laboratory DOIs; medRxiv uses the same 10.1101 prefix).
_BIORXIV_DOI_PREFIX = "10.1101/"

CROSSREF_SEARCH_QUERIES = [
    "BirdCLEF bird sound",
    "bird vocalization bioacoustics",
    "passive acoustic monitoring birds",
    "bird call classification",
    "avian acoustic deep learning",
    "bird species audio identification",
    "soundscape ecology bird",
    "ecoacoustics bird species",
]

# ---------------------------------------------------------------------------
# Papers With Code
# ---------------------------------------------------------------------------

PWC_API_BASE = "https://paperswithcode.com/api/v1/papers/"
PWC_PAGE_SIZE = 50

PWC_SEARCH_QUERIES = [
    "BirdCLEF",
    "bird sound recognition",
    "bird vocalization",
    "bioacoustics bird",
    "passive acoustic monitoring birds",
    "avian sound classification",
]

# ---------------------------------------------------------------------------
# Shared
# ---------------------------------------------------------------------------

# Earliest date to consider (start of modern LifeCLEF/BirdCLEF era).
HISTORY_START = date(2016, 1, 1)

CSV_FIELDNAMES = [
    # "arxiv_id" is the unique key used across all sources.  Non-arXiv papers
    # use a prefixed ID (e.g. "ss:", "dblp:", "biorxiv:", "pwc:") so the field
    # name is a slight misnomer retained for backward compatibility with the
    # existing CSV.  Colons in prefixed IDs are safe for CSV and Python dict keys.
    "arxiv_id",
    "title",
    "authors",
    "submitted",
    "categories",
    "url",
    "abstract",
    "source",
]

# Negative keywords – papers whose title or abstract contain any of these
# phrases (case-insensitive) are excluded from results.
NEGATIVE_KEYWORDS = [
    "text-to-speech",
    "speech synthesis",
    "speaker recognition",
    "speech recognition",
    "music generation",
    "lidar",
    "bird's eye view",
    "autonomous driving",
    "object detection lidar",
    # Medical / clinical audio
    "cochlear implant",
    "sleep apnea",
    "epilepsy",
    "heart sound",
    "lung sound",
    "breath sound",
    "electroencephalogram",
    "electrocardiogram",
    # Plant / microbial biology
    "pangenome",
]

# Positive keywords – at least one of these phrases (case-insensitive) must
# appear in a paper's title or abstract for it to be included.  This keeps
# the collection focused on bird, reptile, insect, and mammal acoustics.
POSITIVE_KEYWORDS = [
    # ----- Birds -----
    "bird", "avian", "ornitholog", "songbird", "raptor",
    "owl", "warbler", "finch", "sparrow", "thrush", "wren", "robin",
    "hawk", "eagle", "parrot", "pigeon", "dove", "hummingbird",
    "woodpecker", "kingfisher", "penguin", "albatross", "seabird",
    "shorebird", "waterfowl", "duck", "goose", "heron", "egret", "crane",
    "stork", "ibis", "flamingo", "pelican", "cormorant", "gannet",
    "swift", "swallow", "nightjar", "cuckoo", "hornbill", "toucan",
    "macaw", "cockatoo", "lark", "bunting", "crossbill", "flycatcher",
    "vireo", "tanager", "blackbird", "starling", "magpie", "crow",
    "raven", "jay", "nuthatch", "treecreeper", "firecrest", "goldcrest",
    "chiffchaff", "oystercatcher", "passerine", "avifauna", "syrinx",
    "burung", "kicau",
    # ----- Mammals -----
    "mammal", "bat ", "bats ", "cetacean", "dolphin", "whale", "porpoise",
    "elephant", "primate", "monkey", "ape", "gibbon",
    "wolf", "wolves", "coyote", "fox", "deer", "bear", "lion", "tiger",
    "leopard", "cheetah", "seal", "sea lion", "otter", "rodent",
    "squirrel", "rabbit", "hare", "hedgehog", "shrew",
    "bovine", "cattle", "wildlife acoustic", "marine mammal",
    # ----- Insects -----
    "insect", "cricket", "cicada", "grasshopper", "katydid", "bee ",
    "wasp ", "beetle", "moth ", "dragonfly",
    "stridulat", "entomolog", "orthoptera", "mosquito", "beehive",
    "sunn pest",
    # ----- Reptiles -----
    "reptile", "lizard", "snake ", "turtle", "tortoise", "crocodil",
    "gecko", "chameleon", "iguana",
    # ----- Amphibians (commonly included in bioacoustics datasets) -----
    "frog", "toad ", "amphibian", "anuran", "salamander",
    # ----- General animal acoustics / monitoring -----
    "bioacoustic", "ecoacoustic", "soundscape", "animal sound",
    "animal call", "animal vocal", "wildlife sound", "wildlife call",
    "wildlife monitor", "passive acoustic monitor",
    "species identif", "species classif", "species recogni",
    "species detect", "species sound", "species acoustic",
    "xeno-canto", "birdclef", "birdnet", "lifeclef",
    "vocaliz", "acoustic index", "acoustic indices", "biosound",
    "natural sound", "acoustic monitoring", "autonomous recording unit",
    "vertebrate", "biodiversity", "communication mask",
]

# Delay between API requests to respect rate-limit guidance (3 s).
API_DELAY_SECONDS = 3

# Number of results to fetch per arXiv API page.
PAGE_SIZE = 100


# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------


def _build_query(keywords: str, start_date: date, end_date: date) -> str:
    """Return a URL-encoded arXiv API query string."""
    # Date range filter: submittedDate:[YYYYMMDD TO YYYYMMDD]
    date_filter = (
        f"submittedDate:[{start_date.strftime('%Y%m%d')}0000"
        f" TO {end_date.strftime('%Y%m%d')}2359]"
    )
    # Title + abstract search
    term = f'(ti:"{keywords}" OR abs:"{keywords}") AND {date_filter}'
    return term


def _fetch_page(query: str, start: int, max_results: int) -> ET.Element:
    """Fetch one page of arXiv results and return the parsed XML root."""
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API_BASE}?{params}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = resp.read()
            return ET.fromstring(data)
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** (attempt + 1) * API_DELAY_SECONDS, 30)
            print(f"  [warn] request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch arXiv page after 5 attempts: {url}")


def _parse_entry(entry: ET.Element) -> dict | None:
    """Parse a single <entry> element into a paper dict."""
    arxiv_id_raw = entry.findtext("atom:id", namespaces=NS) or ""
    # e.g. http://arxiv.org/abs/2008.10010v1 → 2008.10010
    arxiv_id = re.sub(r"v\d+$", "", arxiv_id_raw.split("/abs/")[-1]).strip()
    if not arxiv_id:
        return None

    title = re.sub(r"\s+", " ", entry.findtext("atom:title", namespaces=NS) or "").strip()

    authors = ", ".join(
        (a.findtext("atom:name", namespaces=NS) or "").strip()
        for a in entry.findall("atom:author", namespaces=NS)
    )

    published_raw = entry.findtext("atom:published", namespaces=NS) or ""
    submitted = published_raw[:10]  # YYYY-MM-DD

    categories = " ".join(
        cat.get("term", "")
        for cat in entry.findall("atom:category", namespaces=NS)
    )

    url = f"https://arxiv.org/abs/{arxiv_id}"

    abstract = re.sub(
        r"\s+",
        " ",
        entry.findtext("atom:summary", namespaces=NS) or "",
    ).strip()

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": categories,
        "url": url,
        "abstract": abstract,
        "source": "arxiv",
    }


_NEGATIVE_KEYWORDS_LOWER = [kw.lower() for kw in NEGATIVE_KEYWORDS]
_POSITIVE_KEYWORDS_LOWER = [kw.lower() for kw in POSITIVE_KEYWORDS]


def _is_excluded(paper: dict) -> bool:
    """Return True if the paper matches any negative keyword."""
    haystack = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    return any(kw in haystack for kw in _NEGATIVE_KEYWORDS_LOWER)


def _is_relevant(paper: dict) -> bool:
    """Return True if the paper matches at least one positive keyword.

    Papers that contain none of the animal-acoustics positive keywords are
    considered off-topic and should be excluded from the collection, which is
    focused on bird, reptile, insect, and mammal acoustics.
    """
    haystack = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    return any(kw in haystack for kw in _POSITIVE_KEYWORDS_LOWER)


def fetch_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return all papers matching *keywords* within [start_date, end_date]."""
    query = _build_query(keywords, start_date, end_date)
    papers: list[dict] = []
    start = 0

    while True:
        root = _fetch_page(query, start=start, max_results=PAGE_SIZE)

        total_el = root.find("opensearch:totalResults", {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"})
        total = int(total_el.text) if total_el is not None and total_el.text else 0

        entries = root.findall("atom:entry", namespaces=NS)
        if not entries:
            break

        for entry in entries:
            paper = _parse_entry(entry)
            if paper:
                papers.append(paper)

        start += len(entries)
        if start >= total or len(entries) < PAGE_SIZE:
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------


def load_existing_papers() -> dict[str, dict]:
    """Load papers from CSV, keyed by arxiv_id."""
    if not PAPERS_CSV.exists():
        return {}
    with PAPERS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        result: dict[str, dict] = {}
        for row in reader:
            # Back-fill 'source' for rows written before the field was added.
            if not row.get("source"):
                row["source"] = "arxiv"
            result[row["arxiv_id"]] = row
        return result


def save_papers(papers_by_id: dict[str, dict]) -> None:
    """Write all papers to CSV sorted by submitted date (newest first)."""
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)
    with PAPERS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=CSV_FIELDNAMES,
            extrasaction="ignore",
            restval="",
        )
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# Semantic Scholar helpers
# ---------------------------------------------------------------------------


def _ss_fetch_page(params: dict) -> dict:
    """Fetch one page from the Semantic Scholar bulk-search API."""
    url = f"{SS_BULK_API}?{urllib.parse.urlencode(params)}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** (attempt + 1) * API_DELAY_SECONDS, 30)
            print(f"  [warn] SS request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch Semantic Scholar page after 5 attempts: {url}")


def _ss_item_to_dict(item: dict) -> dict | None:
    """Convert a Semantic Scholar paper item to our paper dict."""
    paper_id = item.get("paperId") or ""
    if not paper_id:
        return None

    title = (item.get("title") or "").strip()
    if not title:
        return None

    external_ids = item.get("externalIds") or {}
    arxiv_id = external_ids.get("ArXiv") or ""

    # If the paper is on arXiv, use its arXiv ID as the primary key so it
    # deduplicates correctly against arXiv-sourced entries.
    if arxiv_id:
        uid = arxiv_id
        url = f"https://arxiv.org/abs/{arxiv_id}"
        source = "arxiv"
    else:
        doi = external_ids.get("DOI") or ""
        uid = f"ss:{paper_id}"
        oa = item.get("openAccessPdf") or {}
        if oa.get("url"):
            url = oa["url"]
        elif doi:
            url = f"https://doi.org/{doi}"
        else:
            url = f"https://www.semanticscholar.org/paper/{paper_id}"
        source = "semanticscholar"

    authors = ", ".join(
        (a.get("name") or "").strip() for a in (item.get("authors") or [])
    )

    pub_date = item.get("publicationDate") or ""
    if pub_date:
        submitted = pub_date[:10]
    else:
        year = item.get("year")
        submitted = f"{year}-01-01" if year else ""

    abstract = re.sub(r"\s+", " ", item.get("abstract") or "").strip()

    return {
        "arxiv_id": uid,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": "",
        "url": url,
        "abstract": abstract,
        "source": source,
    }


def fetch_ss_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return papers from Semantic Scholar matching *keywords* in date range."""
    date_filter = (
        f"{start_date.strftime('%Y-%m-%d')}:{end_date.strftime('%Y-%m-%d')}"
    )
    papers: list[dict] = []
    token: str | None = None

    while True:
        params: dict[str, str] = {
            "query": keywords,
            "fields": SS_FIELDS,
            "publicationDateOrYear": date_filter,
            "sort": "publicationDate:desc",
        }
        if token:
            params["token"] = token

        data = _ss_fetch_page(params)

        for item in data.get("data") or []:
            paper = _ss_item_to_dict(item)
            if paper:
                papers.append(paper)

        token = data.get("token")
        if not token or not data.get("data"):
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# DBLP helpers (CEUR-WS LifeCLEF / BirdCLEF working notes)
# ---------------------------------------------------------------------------


def _dblp_fetch_page(keywords: str, first: int) -> dict:
    """Fetch one page from the DBLP search API."""
    params = urllib.parse.urlencode(
        {
            "q": keywords,
            "format": "json",
            "h": DBLP_PAGE_SIZE,
            "f": first,
        }
    )
    url = f"{DBLP_API_BASE}?{params}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** (attempt + 1) * API_DELAY_SECONDS, 30)
            print(f"  [warn] DBLP request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch DBLP page after 5 attempts: {url}")


def _dblp_info_to_dict(info: dict) -> dict | None:
    """Convert a DBLP hit's ``info`` dict to our paper dict."""
    dblp_key = info.get("key") or ""
    if not dblp_key:
        return None

    title = (info.get("title") or "").strip().rstrip(".")
    if not title:
        return None

    # Electronic edition URL (PDF or proceedings page).
    ee = info.get("ee") or ""
    if isinstance(ee, list):
        ee = ee[0] if ee else ""
    if not ee:
        # Fall back to the DBLP record page.
        ee = info.get("url") or ""
    if not ee:
        return None

    year = str(info.get("year") or "")
    submitted = f"{year}-01-01" if year else ""

    authors_raw = (info.get("authors") or {}).get("author") or []
    if isinstance(authors_raw, dict):
        authors_raw = [authors_raw]
    author_names: list[str] = []
    for a in authors_raw:
        if isinstance(a, str):
            author_names.append(a)
        elif isinstance(a, dict):
            author_names.append(a.get("text") or a.get("$") or "")
    authors = ", ".join(n for n in author_names if n)

    return {
        "arxiv_id": f"dblp:{dblp_key}",
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": "",
        "url": ee,
        "abstract": "",  # DBLP does not expose abstracts
        "source": "ceur-ws",
    }


def fetch_dblp_papers(keywords: str) -> list[dict]:
    """Return all DBLP papers matching *keywords* (no date filter)."""
    papers: list[dict] = []
    first = 0

    while True:
        data = _dblp_fetch_page(keywords, first)
        hits = (data.get("result") or {}).get("hits") or {}
        total_str = hits.get("@total") or "0"
        total = int(total_str)
        hit_list = hits.get("hit") or []
        if isinstance(hit_list, dict):
            hit_list = [hit_list]
        if not hit_list:
            break

        for hit in hit_list:
            info = (hit if isinstance(hit, dict) else {}).get("info") or {}
            paper = _dblp_info_to_dict(info)
            if paper:
                papers.append(paper)

        first += len(hit_list)
        if first >= total or len(hit_list) < DBLP_PAGE_SIZE:
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# bioRxiv helpers (via Crossref API)
# ---------------------------------------------------------------------------


def _crossref_fetch_page(keywords: str, date_filter: str, offset: int) -> dict:
    """Fetch one page from the Crossref API."""
    params = urllib.parse.urlencode(
        {
            "query": keywords,
            "filter": date_filter,
            "select": "DOI,title,author,abstract,posted,created,URL",
            "rows": CROSSREF_PAGE_SIZE,
            "offset": offset,
            "mailto": CROSSREF_MAILTO,
        }
    )
    url = f"{CROSSREF_API_BASE}?{params}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** (attempt + 1) * API_DELAY_SECONDS, 30)
            print(f"  [warn] Crossref request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch Crossref page after 5 attempts: {url}")


def _crossref_item_to_dict(item: dict) -> dict | None:
    """Convert a Crossref work item to our paper dict (bioRxiv only)."""
    doi = (item.get("DOI") or "").strip()
    if not doi or not doi.startswith(_BIORXIV_DOI_PREFIX):
        return None

    titles = item.get("title") or []
    title = titles[0].strip() if titles else ""
    if not title:
        return None

    uid = f"biorxiv:{doi.removeprefix(_BIORXIV_DOI_PREFIX)}"

    authors_list = item.get("author") or []
    authors = ", ".join(
        f"{a.get('given', '')} {a.get('family', '')}".strip()
        for a in authors_list
    )

    # Prefer 'posted' date (bioRxiv first-posted) over 'created'.
    date_info = item.get("posted") or item.get("created") or {}
    date_parts = (date_info.get("date-parts") or [[]])[0]
    if len(date_parts) >= 3:
        submitted = f"{date_parts[0]:04d}-{date_parts[1]:02d}-{date_parts[2]:02d}"
    elif len(date_parts) == 2:
        submitted = f"{date_parts[0]:04d}-{date_parts[1]:02d}-01"
    elif len(date_parts) == 1:
        submitted = f"{date_parts[0]:04d}-01-01"
    else:
        submitted = ""

    url = item.get("URL") or f"https://doi.org/{doi}"

    # Strip JATS XML tags that Crossref embeds in abstracts.
    abstract_raw = item.get("abstract") or ""
    abstract = re.sub(r"<[^>]+>", "", abstract_raw)
    abstract = re.sub(r"\s+", " ", abstract).strip()

    return {
        "arxiv_id": uid,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": "",
        "url": url,
        "abstract": abstract,
        "source": "biorxiv",
    }


def fetch_crossref_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return bioRxiv preprints from Crossref matching *keywords* in date range."""
    date_filter = (
        "type:posted-content,"
        f"from-posted-date:{start_date.strftime('%Y-%m-%d')},"
        f"until-posted-date:{end_date.strftime('%Y-%m-%d')}"
    )
    papers: list[dict] = []
    offset = 0

    while True:
        data = _crossref_fetch_page(keywords, date_filter, offset)
        message = data.get("message") or {}
        total = int(message.get("total-results") or 0)
        items = message.get("items") or []

        if not items:
            break

        for item in items:
            paper = _crossref_item_to_dict(item)
            if paper:
                papers.append(paper)

        offset += len(items)
        if offset >= total or len(items) < CROSSREF_PAGE_SIZE:
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# Papers With Code helpers
# ---------------------------------------------------------------------------


def _pwc_fetch_page(keywords: str, page: int) -> dict:
    """Fetch one page from the Papers With Code API."""
    params = urllib.parse.urlencode(
        {
            "q": keywords,
            "items_per_page": PWC_PAGE_SIZE,
            "page": page,
            "ordering": "-published",
        }
    )
    url = f"{PWC_API_BASE}?{params}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** (attempt + 1) * API_DELAY_SECONDS, 30)
            print(f"  [warn] PwC request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch Papers With Code page after 5 attempts: {url}")


def _pwc_item_to_dict(item: dict) -> dict | None:
    """Convert a Papers With Code result item to our paper dict."""
    title = (item.get("title") or "").strip()
    if not title:
        return None

    arxiv_id = (item.get("arxiv_id") or "").strip()
    if arxiv_id:
        # Normalise to bare ID (strip any version suffix like v2).
        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
        uid = arxiv_id
        url = f"https://arxiv.org/abs/{arxiv_id}"
        source = "arxiv"
    else:
        pwc_id = (item.get("id") or "").strip()
        if not pwc_id:
            return None
        uid = f"pwc:{pwc_id}"
        url = item.get("url_abs") or f"https://paperswithcode.com/paper/{pwc_id}"
        source = "paperswithcode"

    authors_raw = item.get("authors") or []
    authors = ", ".join(str(a) for a in authors_raw)

    submitted = (item.get("published") or item.get("date") or "")[:10]

    abstract = re.sub(r"\s+", " ", item.get("abstract") or "").strip()

    return {
        "arxiv_id": uid,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": "",
        "url": url,
        "abstract": abstract,
        "source": source,
    }


def fetch_pwc_papers(keywords: str, start_date: date) -> list[dict]:
    """Return Papers With Code results matching *keywords* since *start_date*."""
    papers: list[dict] = []
    page = 1

    while True:
        data = _pwc_fetch_page(keywords, page)
        results = data.get("results") or []

        if not results:
            break

        stop_early = False
        for item in results:
            paper = _pwc_item_to_dict(item)
            if paper:
                pub = paper.get("submitted") or ""
                # PwC results are newest-first; stop once we're before start_date.
                if pub and pub[:10] < start_date.strftime("%Y-%m-%d"):
                    stop_early = True
                    break
                papers.append(paper)

        page += 1
        if stop_early or not data.get("next"):
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# Shared fetch helper
# ---------------------------------------------------------------------------


def _ingest(
    new_papers: list[dict],
    existing: dict[str, dict],
) -> int:
    """Add *new_papers* to *existing*, skipping duplicates and excluded entries.

    Returns the number of newly added papers.
    """
    count = 0
    for paper in new_papers:
        pid = paper["arxiv_id"]
        # Duplicate check first (O(1)) before the more expensive keyword scans.
        if pid not in existing and not _is_excluded(paper) and _is_relevant(paper):
            existing[pid] = paper
            count += 1
            print(f"  + {pid}: {paper['title'][:70]}")
    return count


# ---------------------------------------------------------------------------
# README helpers
# ---------------------------------------------------------------------------

_TABLE_START = "<!-- PAPERS_TABLE_START -->"
_TABLE_END = "<!-- PAPERS_TABLE_END -->"


def _build_table(papers_by_id: dict[str, dict]) -> str:
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)

    # Group by year (newest first).
    by_year: dict[str, list] = defaultdict(list)
    for row in rows:
        year = row.get("submitted", "")[:4] or "Unknown"
        by_year[year].append(row)

    sections: list[str] = []
    for year in sorted(by_year.keys(), reverse=True):
        section_lines = [f"### {year}", ""]
        for row in by_year[year]:
            # Truncate long author lists for readability
            authors = row.get("authors", "")
            if authors.count(",") >= 4:
                authors = ", ".join(authors.split(", ")[:4]) + " et al."
            date_str = row.get("submitted", "")[:10]
            abstract = row.get("abstract", "").strip()
            title = row["title"]
            url = row["url"]

            section_lines.append(f"#### [{title}]({url})")
            section_lines.append(f"**{authors}** · {date_str}")
            section_lines.append("")
            if abstract:
                section_lines.append("<details>")
                section_lines.append("<summary>Abstract</summary>")
                section_lines.append("")
                section_lines.append(abstract)
                section_lines.append("")
                section_lines.append("</details>")
                section_lines.append("")
            else:
                section_lines.append("")

        sections.append("\n".join(section_lines))

    return "\n\n".join(sections)


def update_readme(papers_by_id: dict[str, dict]) -> None:
    """Regenerate the paper table in README.md."""
    if not README_MD.exists():
        return

    content = README_MD.read_text(encoding="utf-8")
    table = _build_table(papers_by_id)
    new_section = f"{_TABLE_START}\n{table}\n{_TABLE_END}"

    if _TABLE_START in content:
        # Replace existing table
        pattern = re.compile(
            re.escape(_TABLE_START) + r".*?" + re.escape(_TABLE_END),
            re.DOTALL,
        )
        content = pattern.sub(lambda _: new_section, content)
    else:
        # Append after the first paragraph
        content = content.rstrip() + "\n\n" + new_section + "\n"

    README_MD.write_text(content, encoding="utf-8")
    print(f"README updated with {len(papers_by_id)} papers.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch BirdCLEF papers from arXiv and other sources."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--full",
        action="store_true",
        help=f"Fetch all papers since {HISTORY_START} (historical back-fill).",
    )
    mode.add_argument(
        "--days",
        type=int,
        default=8,
        metavar="N",
        help="Fetch papers from the last N days (default: 8, for weekly cron).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    today = datetime.now(tz=timezone.utc).date()

    if args.full:
        start_date = HISTORY_START
        end_date = today
        print(f"Full historical fetch: {start_date} → {end_date}")
    else:
        start_date = today - timedelta(days=args.days)
        end_date = today
        print(f"Incremental fetch (last {args.days} days): {start_date} → {end_date}")

    existing = load_existing_papers()
    print(f"Loaded {len(existing)} existing papers from {PAPERS_CSV.name}.")

    # Remove any previously saved papers that match negative keywords.
    before = len(existing)
    existing = {pid: p for pid, p in existing.items() if not _is_excluded(p)}
    removed = before - len(existing)
    if removed:
        print(f"Removed {removed} existing paper(s) matching negative keywords.")

    # Remove any previously saved papers that lack animal-acoustics content.
    before = len(existing)
    existing = {pid: p for pid, p in existing.items() if _is_relevant(p)}
    removed_irrelevant = before - len(existing)
    if removed_irrelevant:
        print(
            f"Removed {removed_irrelevant} existing paper(s) not related to "
            "animal acoustics."
        )
    removed += removed_irrelevant

    new_count = 0

    # ------------------------------------------------------------------
    # arXiv
    # ------------------------------------------------------------------
    print("\n\n=== arXiv ===")
    for keywords in ARXIV_SEARCH_QUERIES:
        print(f"\nQuerying arXiv for: {keywords!r} …")
        try:
            papers = fetch_papers(keywords, start_date, end_date)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue
        new_count += _ingest(papers, existing)
        time.sleep(API_DELAY_SECONDS)

    # ------------------------------------------------------------------
    # Semantic Scholar
    # ------------------------------------------------------------------
    print("\n\n=== Semantic Scholar ===")
    for keywords in SS_SEARCH_QUERIES:
        print(f"\nQuerying Semantic Scholar for: {keywords!r} …")
        try:
            papers = fetch_ss_papers(keywords, start_date, end_date)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue
        new_count += _ingest(papers, existing)
        time.sleep(API_DELAY_SECONDS)

    # ------------------------------------------------------------------
    # DBLP / CEUR-WS (no date filter – deduplicate handles repeats)
    # ------------------------------------------------------------------
    print("\n\n=== DBLP (CEUR-WS working notes) ===")
    for keywords in DBLP_SEARCH_QUERIES:
        print(f"\nQuerying DBLP for: {keywords!r} …")
        try:
            papers = fetch_dblp_papers(keywords)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue
        new_count += _ingest(papers, existing)
        time.sleep(API_DELAY_SECONDS)

    # ------------------------------------------------------------------
    # bioRxiv via Crossref
    # ------------------------------------------------------------------
    print("\n\n=== bioRxiv (Crossref) ===")
    for keywords in CROSSREF_SEARCH_QUERIES:
        print(f"\nQuerying Crossref/bioRxiv for: {keywords!r} …")
        try:
            papers = fetch_crossref_papers(keywords, start_date, end_date)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue
        new_count += _ingest(papers, existing)
        time.sleep(API_DELAY_SECONDS)

    # ------------------------------------------------------------------
    # Papers With Code
    # ------------------------------------------------------------------
    print("\n\n=== Papers With Code ===")
    for keywords in PWC_SEARCH_QUERIES:
        print(f"\nQuerying Papers With Code for: {keywords!r} …")
        try:
            papers = fetch_pwc_papers(keywords, start_date)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue
        new_count += _ingest(papers, existing)
        time.sleep(API_DELAY_SECONDS)

    print(f"\nFound {new_count} new papers. Total: {len(existing)}.")

    if new_count > 0 or removed > 0 or not PAPERS_CSV.exists():
        save_papers(existing)
        print(f"Saved to {PAPERS_CSV}.")

    update_readme(existing)


if __name__ == "__main__":
    main()
