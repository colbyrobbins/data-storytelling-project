# The Untold Stories in Public Data

A data storytelling project for Module Project 1. Two of us pick a publicly available dataset, dig into it, and turn what we find into a public-facing story — plus the reproducible analysis behind it.

**Status:** dataset and story angle not yet chosen. This README will be filled in as those decisions are made — see the TBD markers below.

## Overview

- **Topic / dataset:** _TBD_
- **Audience — who this story is for and why it matters to them:** _TBD_
- **The story we're telling:** _TBD_

## Deliverables

- **Public communication piece:** _link TBD_ (blog post / podcast / YouTube video / infographic)
- **Presentation:** in class, Sep 29 (8 minutes max) — slides linked from [`presentation/`](presentation/)
- **This repository:** code, data, and documentation for the analysis behind the story

## Dataset

_To fill in once we've picked a dataset:_

- **Source:** 
- **Citation:** 
- **License / usage terms:** 
- **Access:** raw data lives in [`data/raw/`](data/raw/); if it's too large or restricted to commit, see [`data/raw/README.md`](data/raw/README.md) for how to get it instead.

## Project Structure

```
├── data/
│   ├── raw/            # original, unmodified dataset(s) + source/citation info
│   └── processed/      # cleaned data and engineered features produced by src/
├── src/
│   ├── preprocessing.py  # loads raw data, cleans it, writes to data/processed/
│   ├── eda.py            # exploratory analysis + the charts behind our findings
│   └── features.py       # feature engineering used in the analysis
├── notebooks/           # exploratory/scratch notebooks (not a substitute for src/ scripts)
├── reports/
│   └── figures/         # exported charts/visuals used in the public write-up
├── presentation/        # slides for the in-class presentation
├── requirements.txt
└── CONTRIBUTING.md      # team workflow, branch naming, PR rules
```

## Prerequisites

- Python 3.10+
- Git

## Local Setup

Clone the repository:

```bash
git clone https://github.com/colbyrobbins/data-storytelling-project.git
cd data-storytelling-project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate.ps1
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Reproduce the Analysis

Once the dataset is in place, the pipeline runs as:

```bash
python3 src/preprocessing.py   # data/raw/  ->  data/processed/
python3 src/features.py        # adds engineered features to data/processed/
python3 src/eda.py             # generates the charts saved to reports/figures/
```

(Exact commands/arguments will be updated here once these scripts are built out.)

## Team Workflow

1. Pull the latest `main`.
2. Create a branch for your task.
3. Make and test your changes.
4. Commit with a clear message.
5. Push your branch and open a pull request.
6. Ask your teammate to review it.
7. Merge only after review.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details, including branch naming and team rules.

## Ethics & Limitations

_To fill in during/after EDA: known biases or gaps in the data, who might be over/under-represented, and any caveats readers should keep in mind when interpreting the story._

## License

MIT — see [LICENSE](LICENSE).
