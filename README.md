# Analysis Pipeline

This repository drives [analysis.castromedia.org](https://analysis.castromedia.org), a fully transparent data workflow.

1. **Aggregation** – The `data/` folder stores every raw dataset. A notebook called `update.ipynb` pulls from each source on a schedule, versioning the files and opening a pull request with the changes.
2. **Analysis** – Jupyter notebooks inside `analysis/` use the latest data snapshots to produce figures and markdown reports. When data changes, these notebooks re-run automatically and propose another pull request.
3. **Publication** – Once both pull requests are merged automatically (assuming no conflicts), GitHub Pages rebuilds the site using Jekyll. The rendered HTML lives in this repo so anyone can inspect the exact inputs and outputs.
4. **Metadata** – Every dataset directory now ships with a `metadata.md` file capturing the catalog fields and a short description. Analysis folders include a similar `metadata.md` listing the result columns. The homepage reads these files to populate its project and dataset lists.

This setup aggregates data from many sources, analyzes it, and publishes the results in real time. Because every step happens in the open through Git commits and PRs, it offers a maximally transparent workflow for public research.

## Pipelines

These analysis drive the content behind the public properties which function as a mass consumption format for the data:
- [**TopStoryReview:**](https://topstoryreview.com) pulls the most recent output of the [news topics](https://github.com/Castro-Media/Analysis/blob/main/analysis/news-topics/top.json) analysis and basically builds a website around those headlines.

News feeds are organized by region under `data/news/<region>/<source>/`. Each of those directories has its own `metadata.md` describing the source so analyses and the homepage can find them easily.
