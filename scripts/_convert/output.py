"""Write per-paper markdown files with YAML frontmatter."""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml


@dataclass
class PaperRecord:
    """Everything needed to render a per-paper markdown file."""

    arxiv_id: str
    title: str
    authors: list[str]
    submitted: str  # YYYY-MM-DD
    categories: list[str]
    arxiv_url: str
    source: str  # "latex" | "pdf" | "metadata-only"
    converter: str  # "pandoc" | "marker" | "none"
    body: str  # already-rendered markdown body (no frontmatter, no h1)
    references_parsed: int
    citations_resolved: str  # e.g. "27/41"
    github_repo: str = ""  # linked repo from the paper's Hugging Face page
    arxiv_version: str = ""
    llm_remediated: bool = False
    citations_resolved_at: str = field(
        default_factory=lambda: datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    )


def paper_slug(arxiv_id: str) -> str:
    """Return a filesystem-safe filename stem for a paper id.

    Bare arXiv ids (``2607.14072``) and prefixed ids (``ss:<hex>``,
    ``biorxiv:<doi-suffix>``) are already path-safe. DBLP / Papers-With-Code
    keys can embed ``/`` (e.g. ``dblp:conf/clef/Foo25``), which would spill the
    file across nested directories, so slashes are flattened to underscores.
    """
    return arxiv_id.replace("/", "_")


def paper_path(arxiv_id: str, submitted: str, papers_root: Path) -> Path:
    """Return the destination path for a paper's markdown file."""
    year = submitted[:4]
    return papers_root / year / f"{paper_slug(arxiv_id)}.md"


def write_paper_markdown(record: PaperRecord, papers_root: Path) -> Path:
    """Write *record* to ``papers_root/<year>/<arxiv_id>.md`` and return the path."""
    path = paper_path(record.arxiv_id, record.submitted, papers_root)
    path.parent.mkdir(parents=True, exist_ok=True)

    front = {
        "arxiv_id": record.arxiv_id,
        "title": record.title,
        "authors": record.authors,
        "submitted": record.submitted,
        "categories": record.categories,
        "arxiv_url": record.arxiv_url,
        "github_repo": record.github_repo,
        "source": record.source,
        "converter": record.converter,
        "llm_remediated": record.llm_remediated,
        "citations_resolved": record.citations_resolved,
        "citations_resolved_at": record.citations_resolved_at,
        "references_parsed": record.references_parsed,
        "arxiv_version": record.arxiv_version,
    }
    front_yaml = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)

    body = unicodedata.normalize("NFC", record.body).rstrip() + "\n"
    text = f"---\n{front_yaml}---\n\n{body}"
    path.write_text(text, encoding="utf-8")
    return path
