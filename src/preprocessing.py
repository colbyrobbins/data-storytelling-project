"""
preprocessing.py

Loads the raw dataset from data/raw/, cleans it (handles missing values,
fixes types, drops/renames columns as needed), and writes the cleaned
result to data/processed/.

TODO: once a dataset is chosen, implement load_raw(), clean(), and
save_processed() below and update the file paths.
"""

from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"


def load_raw():
    """Read the raw dataset(s) from RAW_DIR. TODO: implement."""
    raise NotImplementedError


def clean(df):
    """Clean/validate the raw dataframe. TODO: implement."""
    raise NotImplementedError


def save_processed(df, filename="cleaned.csv"):
    """Write the cleaned dataframe to PROCESSED_DIR."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / filename, index=False)


def main():
    df = load_raw()
    df = clean(df)
    save_processed(df)


if __name__ == "__main__":
    main()
