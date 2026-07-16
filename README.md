# birdclef-papers

A curated, automatically-updated collection of papers on **bird sound recognition**, bioacoustics, passive acoustic monitoring, and related animal-sound topics — covering the BirdCLEF / LifeCLEF competition era (2016 onwards) and growing every day.

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

- Papers are sourced from multiple indexes via their public APIs:
  - [arXiv](https://arxiv.org/) — preprints in cs, eess, and q-bio.
  - [Semantic Scholar](https://www.semanticscholar.org/) — broad coverage of journals and conferences not on arXiv.
  - [DBLP](https://dblp.org/) / [CEUR-WS](https://ceur-ws.org/) — LifeCLEF and BirdCLEF workshop working-notes.
  - [bioRxiv](https://www.biorxiv.org/) (via [Crossref](https://www.crossref.org/)) — ecology and bioacoustics preprints.
  - [Papers With Code](https://paperswithcode.com/) — community-curated ML papers.
- A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull recently submitted papers.
- Results are filtered with a negative-keyword blacklist plus a positive animal-acoustics relevance gate (birds, mammals, insects, reptiles, amphibians).
- The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- For arXiv papers, converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
- Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
- For Semantic Scholar entries, an open-access PDF is converted with marker when one is available.
- bioRxiv, CEUR-WS working-notes, and Papers With Code entries without a fetchable source are written as metadata-only stubs (title, authors, abstract).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.
- When the paper's [Hugging Face page](https://huggingface.co/papers) links a GitHub repo, it is recorded as `github_repo` in the frontmatter.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata (`github_repo`, …) + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc and Node (for Prettier, which normalizes the generated markdown):

```bash
# macOS
brew install pandoc node

# Ubuntu
sudo apt-get install pandoc nodejs npm
```

```bash
# Install the pinned Prettier used by the pipeline, CI, and pre-commit
npm ci

# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2016-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library (plus a Prettier pass on the README); the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager). Both scripts format the markdown they generate with the repo-pinned [Prettier](https://prettier.io/) (`npm ci`), and a [Format workflow](.github/workflows/format.yml) enforces it on every PR.

## Triggering a manual update

Open the **Actions** tab → **Fetch BirdCLEF Papers** → **Run workflow**.
Select _full = true_ to back-fill from 2016 and rebuild all paper markdown, or leave it as _false_ for an incremental update.

## Search terms

Papers are discovered by querying each source with the keyword sets below.

**arXiv** · `BirdCLEF` · `bird sound recognition` · `bird call recognition` · `bird song recognition` · `bird species identification audio` · `bird vocalization classification` · `avian sound classification` · `bioacoustics deep learning` · `passive acoustic monitoring birds` · `soundscape bird` · `bird audio detection` · `bird species classification spectrogram` · `ecoacoustics machine learning` · `bird call detection` · `LifeCLEF bird` · `BirdNET` · `xeno-canto` · `avian bioacoustics` · `bird acoustic identification` · `automated bird identification` · `bird sound classification deep learning` · `bird species acoustic` · `soundscape ecology machine learning` · `wildlife acoustic monitoring` · `ornithology deep learning` · `bird audio neural network` · `avian call classification` · `bird sound event detection` · `bird sound dataset` · `PAM birds` · `bird species recognition neural` · `mel spectrogram bird classification`

**Semantic Scholar** · `BirdCLEF` · `bird sound recognition` · `bird vocalization classification` · `avian bioacoustics deep learning` · `passive acoustic monitoring birds` · `LifeCLEF bird` · `BirdNET bird identification` · `bird call classification neural network` · `bird species audio identification` · `soundscape ecology bird machine learning` · `ecoacoustics bird deep learning` · `automated bird species recognition`

**DBLP / CEUR-WS** · `BirdCLEF` · `LifeCLEF bird` · `bird sound recognition CLEF` · `avian sound classification CLEF` · `bird species identification audio CLEF` · `passive acoustic monitoring LifeCLEF`

**bioRxiv** · `BirdCLEF bird sound` · `bird vocalization bioacoustics` · `passive acoustic monitoring birds` · `bird call classification` · `avian acoustic deep learning` · `bird species audio identification` · `soundscape ecology bird` · `ecoacoustics bird species`

**Papers With Code** · `BirdCLEF` · `bird sound recognition` · `bird vocalization` · `bioacoustics bird` · `passive acoustic monitoring birds` · `avian sound classification`

## Papers

<!-- PAPERS_TABLE_START -->

_Showing the last 30 days (4 of 1623 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [MetaPerch: Learning from metadata for bioacoustics foundation models](https://arxiv.org/abs/2607.14072)

**Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer** · 2026-07-15

<details>
<summary>Abstract</summary>

Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work, we explore the use of metadata -- such as location and time -- as auxiliary supervision signals, allowing the model to leverage species-metadata correlations in its learned representation. Auxiliary metadata losses provide additional information beyond vocalizations alone that can encourage a richer, more robust representation that generalizes better to species distribution and acoustic domain shifts -- important challenges for deployment in real-world passive acoustic monitoring (PAM) settings. We introduce MetaPerch, a new foundation model that achieves strong species identification performance across multiple challenging domains and present an extensive empirical study of the effects of 9 diverse metadata sources on 17 bioacoustic datasets.

</details>

#### [Two-stage fine-tuning of HuBERT for multi-label bird species recognition in overlapping acoustic environments](https://doi.org/10.1007/s11047-026-10080-x)

**Hailemariam Abebe Endalamaw, Chuan-Kai Yang** · 2026-07-13

<details>
<summary>Abstract</summary>

Automated recognition of bird species from audio is critical for biodiversity monitoring, yet it remains difficult in practice because field recordings often contain multiple birds vocalizing at the same time, strong environmental noise, and limited labeled data. Most existing systems either assume single-species recordings, require clean inputs, or depend on manually engineered preprocessing, such as source separation. This work introduces a novel two-stage fine-tuning framework that adapts a large self-supervised speech model (HuBERT) to the highly non-speech, polyphonic, multi-label setting of wild bird soundscapes. The proposed approach departs from conventional direct fine-tuning by using a two-stage curriculum. In Stage 1, HuBERT is fine-tuned on clean single-species recordings to learn discriminative, species-specific acoustic representations without interference. In Stage 2, the model is then transferred and further fine-tuned on synthetically constructed overlapping vocalizations, enabling it to generalize to real noisy soundscapes where multiple species co-occur. This two-stage adaptation strategy bridges the acoustic gap between human speech pretraining and avian bioacoustics, and allows robust multi-label prediction directly on overlapping audio without requiring explicit source separation. Extensive experiments on ten bird species show that the proposed two-stage HuBERT achieves an F1-score of 0.94 on overlapping recordings, outperforming (i) HuBERT variants trained only on clean or overlapping audio, and (ii) state-of-the-art CNN, RNN, graph-based, and transformer baselines reported in prior studies. These results demonstrate that two-stage self-supervised adaptation is an effective and scalable direction for real-time, multi-species bird monitoring in complex natural environments.

</details>

#### [Farmland bird diversity requires heterogeneity between and within habitats](https://doi.org/10.1007/s10980-026-02406-y)

**M. K. Kasten, Thomas Hiller, Sara Tassoni, Rosalie Böhmer et al.** · 2026-07-01

<details>
<summary>Abstract</summary>

Birds are declining worldwide, with farmland birds disproportionately affected. Most studies on farmland birds focus on single habitat types, yet agriculturally dominated landscapes are mosaics composed of multiple habitat types like arable land, grassland, forests, and orchards. We aimed to understand how these habitat types jointly shape farmland bird diversity, particularly regarding local and landscape drivers of alpha and beta diversity. We used passive acoustic monitoring to survey farmland bird communities in 14 mosaic agricultural landscapes (1 km2) in southern Germany that differ in habitat diversity. In total, 224 autonomous recording units were deployed in a grid-based design with sampling intensity proportional to habitat area. Using BirdNET and manual validation, we identified 54 bird species from 2016 h of recordings collected over 4.5 months. Local species richness (alpha diversity) increased with habitat heterogeneity at both local and landscape scales. Arable sites showed the lowest alpha diversity but comparatively high within-habitat beta diversity, whereas orchards supported high alpha but low within-habitat beta diversity. Beta diversity was highest between habitat types, especially between forests and arable land, reflecting strong contrasts in their structural complexity. Generalized dissimilarity modelling showed that local predictors were more important than landscape-level predictors in explaining bird beta diversity. Habitat associations of bird species were largely consistent with ecological expectations: bird species adapted to dense vegetation occurred mainly in forest-dominated sites, while open-habitat species were associated with arable land. Species with decreasing population trends occurred across all major habitat types. At the landscape scale, gamma diversity increased strongly with landscape diversity. Maintaining habitat heterogeneity at multiple spatial scales is critical to conserve farmland bird diversity.

</details>

#### [Bird Species Detection from Audio Signals Using Transfer Learning](https://doi.org/10.22214/ijraset.2026.82931)

**Trishika K, D. R** · 2026-06-30

<details>
<summary>Abstract</summary>

Automatic identification of bird species from audio recordings is an important task in ecological research and biodiversity monitoring. This study proposes a deep learning-based framework that analyzes bird sounds using signal processing and transfer learning techniques. Audio signals are first transformed into frequency-based representations such as Fast Fourier Transform (FFT) and spectrograms. The use of pre-trained networks enhances learning efficiency and improves classification performance. A comparative evaluation between FFT features and spectrogram inputs reveals that spectrogram-based representations capture richer acoustic patterns, leading to better accuracy. The proposed system demonstrates reliable performance and can be effectively used in real-time environmental monitoring applications

</details>

</details>
<!-- PAPERS_TABLE_END -->
