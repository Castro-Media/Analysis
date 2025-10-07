# News Topics Analysis Directory

## Purpose
The `analysis/news-topics` folder generates a ranked view of current news cycles. It consumes the consolidated headline feed maintained in `analysis/headlines`, scores the words that appear across stories, and publishes CSV outputs that can be embedded in the public site.

## Workflow Summary
1. **Notebook orchestration** – `analyze_headlines.ipynb` loads the latest headlines, cleans duplicates, applies scoring, and writes refreshed tables for the site.
2. **Web presentation** – `index.md` is the published page. It documents each processing step and renders the CSV artifacts as interactive tables through the site layout.
3. **Stop-word management** – `exclude.txt` lists terms to ignore when scoring words so that filler language does not dominate the rankings.
4. **Source exclusions** – `exclude_sources.txt` lists publishers to drop only from the final highlight step while still allowing their headlines to influence word scoring.
5. **Result archives** – The `archive/` subdirectory stores timestamped snapshots of every generated `scores`, `rank`, and `top` table for historical comparisons.
6. **Latest outputs** – `scores.csv`, `rank.csv`, `top.csv`, and `top.json` hold the current results that the dashboard consumes.

## Data Flow Details
- Input data arrives via the `analysis/headlines` pipeline, which provides `latest.csv` with deduplicated story metadata.
- The notebook tokenizes each headline, removes stop words, and tallies word frequencies to produce `scores.csv`.
- Headline scores are derived by summing the component word scores, producing `rank.csv`.
- To diversify the highlights, the workflow iteratively removes the dominant word, re-sorts the list, and records the top selections in `top.csv` and `top.json`.
- When the highlight loop encounters a story from a publisher listed in `exclude_sources.txt`, it skips that entry and continues searching so that only approved sources appear in the final `top` files.
- All refreshed CSVs overwrite the root copies while previous versions are appended to `archive/` with timestamped filenames for reproducibility.

## Usage Tips
- Update `exclude.txt` when you notice generic verbs, pronouns, or location names overpowering the topic list.
- Add publisher names to `exclude_sources.txt` when you want to keep their stories out of the highlighted list without affecting their contribution to word scores.
- Review the `archive/` snapshots to audit unexpected shifts in rankings or to rebuild past visualizations.
- Run the notebook end-to-end whenever the headline feed updates so that the published tables stay synchronized with the source data.

