"""Build a per-feed RSS freshness and item-count dashboard."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


def find_repository_root(start_directory: Path) -> Path:
    """Return the repository root containing the data and analysis directories."""
    for directory in [start_directory, *start_directory.parents]:
        has_data = (directory / "data").is_dir()
        has_analysis = (directory / "analysis").is_dir()

        if has_data and has_analysis:
            return directory

    raise FileNotFoundError("Repository root containing data and analysis was not found.")


def read_front_matter(index_path: Path) -> dict[str, str]:
    """Return the simple YAML front matter values from a source index page."""
    index_text = index_path.read_text(encoding="utf-8")
    match = re.search(r"^---\n(.*?)\n---", index_text, re.DOTALL)

    if not match:
        return {}

    metadata: dict[str, str] = {}

    for line in match.group(1).splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", maxsplit=1)
        metadata[key.strip()] = value.strip().strip('"')

    return metadata


def count_latest_entries(latest_path: Path) -> tuple[int, str]:
    """Return the latest feed item count and a status for its JSON payload."""
    if not latest_path.exists():
        return 0, "missing_latest_file"

    try:
        payload = json.loads(latest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0, "invalid_json"

    if not isinstance(payload, dict):
        return 0, "unexpected_payload"

    entries = payload.get("entries")

    if not isinstance(entries, list):
        return 0, "missing_entries"

    if not entries:
        return 0, "empty_entries"

    return len(entries), "ok"


def build_feed_rows(news_directory: Path, repository_root: Path) -> list[dict[str, str | int]]:
    """Collect fetch metadata and item counts for every configured news feed."""
    feed_rows: list[dict[str, str | int]] = []

    for index_path in sorted(news_directory.rglob("index.md")):
        metadata = read_front_matter(index_path)
        filetype = metadata.get("filetype", "").lower()

        if filetype not in {"rss", "xml", "wordpress"}:
            continue

        item_count, latest_status = count_latest_entries(index_path.parent / "latest.json")
        feed_rows.append(
            {
                "feed_path": str(index_path.parent.relative_to(repository_root)),
                "category": metadata.get("category", ""),
                "source": metadata.get("source", ""),
                "title": metadata.get("title", ""),
                "last_fetched": metadata.get("last_fetched", ""),
                "item_count": item_count,
                "latest_status": latest_status,
                "feed_url": metadata.get("url", ""),
            }
        )

    return sorted(feed_rows, key=lambda row: str(row["feed_path"]))


def write_dashboard_csv(feed_rows: list[dict[str, str | int]], output_path: Path) -> None:
    """Write the feed health rows to the dashboard's public CSV file."""
    fieldnames = [
        "feed_path",
        "category",
        "source",
        "title",
        "last_fetched",
        "item_count",
        "latest_status",
        "feed_url",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=fieldnames,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(feed_rows)


def print_dashboard_summary(feed_rows: list[dict[str, str | int]]) -> None:
    """Print a concise count of healthy, empty, and unreadable feed outputs."""
    status_counts = Counter(str(row["latest_status"]) for row in feed_rows)
    populated_count = sum(int(row["item_count"]) > 0 for row in feed_rows)
    total_items = sum(int(row["item_count"]) for row in feed_rows)

    print(f"News feeds: {len(feed_rows)}")
    print(f"Feeds with one or more items: {populated_count}")
    print(f"Items in current latest files: {total_items}")

    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")


def build_dashboard() -> list[dict[str, str | int]]:
    """Create the current news-feed report and return its rows for notebook display."""
    repository_root = find_repository_root(Path.cwd().resolve())
    news_directory = repository_root / "data" / "news"
    project_directory = repository_root / "analysis" / "dashboard"
    feed_rows = build_feed_rows(news_directory, repository_root)

    write_dashboard_csv(feed_rows, project_directory / "latest.csv")
    print_dashboard_summary(feed_rows)

    return feed_rows


if __name__ == "__main__":
    build_dashboard()
