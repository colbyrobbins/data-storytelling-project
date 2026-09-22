# Setting the Record Straight

A data storytelling project investigating trends in Durham Police Department calls and reports.

## Overview

- **Topic / dataset:** DPD Calls for Service (2025)
- **Audience — who this story is for and why it matters to them:** This project aims to provide the Durham community with insights about trends in crime vs crime reporting in their city.
- **The story we're telling:** [something about large majority of calls never reported, and how reporting rate/crime trends change over the year and across the city geographically]

## Deliverables

- **Public communication piece:** Investigative article
- **Presentation:** slides linked from [`presentation/`](presentation/)
- **Github Repository:** code, data, and documentation for the analysis behind the story

## Dataset

- **Source:** City and County of Durham, NC (ArcGIS Online)
- **Citation:** City of Durham, North Carolina. (2025). DPD Calls for Service (2025) [Data set]. Durham Open Data. https://live-durhamnc.opendata.arcgis.com/datasets/c55a356fa8ea49d3a8898c67f9282435/about
- **License / usage terms:** Free public data, no license
- **Access:** raw data lives in [`data/raw/`](data/raw/)

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
