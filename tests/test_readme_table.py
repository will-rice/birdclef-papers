"""Tests for the README table builder in scripts/fetch_papers.py."""

from __future__ import annotations

from datetime import date, timedelta

from scripts.fetch_papers import README_TABLE_LIMIT, _build_table


def _paper(i: int, submitted: str) -> dict:
    return {
        "arxiv_id": f"2401.{i:05d}",
        "title": f"Paper {i}",
        "authors": "A. Author",
        "submitted": submitted,
        "categories": "eess.AS",
        "url": f"https://arxiv.org/abs/2401.{i:05d}",
        "abstract": "An abstract.",
    }


def test_table_shows_only_last_n_papers() -> None:
    papers = {
        p["arxiv_id"]: p
        for p in [
            _paper(i, (date.today() - timedelta(days=i)).isoformat())
            for i in range(1, README_TABLE_LIMIT + 5)
        ]
    }
    table = _build_table(papers)
    assert table.count("#### [") == README_TABLE_LIMIT
    assert f"last {README_TABLE_LIMIT} papers ({README_TABLE_LIMIT} of {README_TABLE_LIMIT + 4} total)" in table
    assert "papers/README.md" in table
