# birdclef-papers

A curated, automatically-updated collection of papers on **bird sound recognition**, bioacoustics, passive acoustic monitoring, and related topics — covering the BirdCLEF Kaggle competition era (2016 onwards) and growing every week.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/) via its public API.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs every **Monday at 06:00 UTC** to pull papers submitted in the previous week.
* The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Running locally

```bash
# Incremental fetch (last 8 days)
python scripts/fetch_papers.py

# Full historical fetch (everything since 2016-01-01)
python scripts/fetch_papers.py --full

# Custom window
python scripts/fetch_papers.py --days 30
```

No third-party dependencies are required — the script uses only the Python standard library.

## Triggering a manual update

Open the **Actions** tab → **Fetch BirdCLEF Papers** → **Run workflow**.  
Select *full = true* to back-fill from 2016, or leave it as *false* for an incremental update.

## Search terms

The following keyword queries are used against arXiv title and abstract fields:

`BirdCLEF` · `bird sound recognition` · `bird call recognition` · `bird song recognition` · `bird species identification audio` · `bird vocalization classification` · `avian sound classification` · `bioacoustics deep learning` · `passive acoustic monitoring birds` · `soundscape bird` · `bird audio detection` · `bird species classification spectrogram` · `ecoacoustics machine learning` · `bird call detection` · `LifeCLEF bird`

## Papers

<!-- PAPERS_TABLE_START -->
<!-- PAPERS_TABLE_END -->
