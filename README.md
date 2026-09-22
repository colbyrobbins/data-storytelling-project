# Setting the Record Straight

A data storytelling project investigating trends in Durham Police Department calls and reports.

An analysis by Jothi Gupta & Colby Robbins for AIPI 510.

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

### Column definitions

| Column | Description |
|---|---|
| `Source` | How the call was initiated (e.g., `Wireless 911 Call`, `Phone Call`, `Self Initiated`, `Radio`, `Alarm Line`, `Texting`). |
| `Priority` | Numeric priority level assigned to the call, `0`–`9` (lower typically indicates higher urgency). |
| `Nature` | Short text description of the reported incident type (e.g., `SOUND OF SHOTS`). |
| `Address` | Street address or intersection where the call originated. |
| `X` | Projected X coordinate (state plane) of the call location. |
| `Y` | Projected Y coordinate (state plane) of the call location. |
| `District` | DPD patrol district handling the call (`D1`–`D5`, or `DSO` for Sheriff's Office). |
| `Disposition` | Outcome recorded for the call (e.g., `Accident Report`, `Citation Issued`, `Cancelled`, `False Alarm`). |
| `Cancelled` | Binary flag (`0`/`1`) indicating whether the call was cancelled before dispatch/resolution. |
| `datetime` | Full timestamp of the call (`YYYY-MM-DD HH:MM:SS`). |
| `hour` | Hour of day the call occurred (0–23), extracted from `datetime`. |
| `day_of_week` | Day of the week the call occurred (e.g., `Wednesday`). |
| `month` | Year-month of the call (`YYYY-MM`), extracted from `datetime`. |
| `date` | Calendar date of the call (`YYYY-MM-DD`), extracted from `datetime`. |
| `report_category` | Classification of `Disposition` into `Crime Report`, `Other Report`, or `No Report`. |
| `crime_report` | Boolean flag, `True` only when `report_category` is `Crime Report`. |
| `filed_report` | Boolean flag, `True` when `report_category` is `Crime Report` or `Other Report` (any formal report filed). |

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
python3 src/map-graphs.py      # generates the dataset used in ArcGis mapping
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
