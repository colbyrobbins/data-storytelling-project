"""
preprocessing.py

Loads the raw dataset from data/raw/, cleans it (handles missing values,
fixes types, drops/renames columns as needed), and writes the cleaned
result to data/processed/.
"""
import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"


def load_raw():
    """Read the raw dataset(s) from RAW_DIR. """
    filepath_calls = RAW_DIR / "dpd_calls_for_service_2025.csv"
    df_calls = pd.read_csv(filepath_calls)
    return df_calls


def clean_calls(df):
    """Clean/validate the raw dataframe."""
    df = df.copy()

    # Drop identifier/geo columns not used downstream, then drop any row with a null
    df.drop(columns=['Event Number', 'Case Number', 'Beat', 'Tract'], inplace=True)
    df = df[df.notnull().all(axis=1)]

    # Combine date + time into a single datetime column
    df['datetime'] = pd.to_datetime(
        df['Call Date'] + ' ' + df['Call Time'],
        format='%m/%d/%Y %I:%M:%S%p'
    )
    df.drop(columns=['Call Date', 'Call Time'], inplace=True)

    # Encode Priority as an ordinal (9 = lowest urgency code -> 0, ... P -> 9)
    df['Priority'] = df['Priority'].map({
        '9': 0,
        '8': 1,
        '7': 2,
        '6': 3,
        '5': 4,
        '4': 5,
        '3': 6,
        '2': 7,
        '1': 8,
        'P': 9
    })

    # Cast categorical columns
    for col in ['Nature', 'District', 'Disposition']:
        df[col] = df[col].astype('category')

    # Drop rows with implausible Durham-area coordinates (raw NC State Plane feet)
    df = df[
        df['X'].between(1_900_000, 2_200_000) &
        df['Y'].between(700_000, 900_000)
    ].copy()

    return df


def save_processed_calls(df, filename="dpd_calls_2025_cleaned.csv"):
    """Write the cleaned dataframe to PROCESSED_DIR."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / filename, index=False)


def main():
    df_calls = load_raw()
    df_calls_cleaned = clean_calls(df_calls)
    save_processed_calls(df_calls_cleaned)


if __name__ == "__main__":
    main()
