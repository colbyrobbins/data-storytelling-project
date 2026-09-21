"""
mapping.py

Further feature engineering to prepare for mapping on the featured dataset in data/processed/. Adds
derived columns/aggregations used in the analysis and re-saves the result.

TODO: once preprocessing.py and features.py is in place, implement load_processed(),
engineer_features(), and save() below.
"""

import pandas as pd
from pathlib import Path
import numpy as np
import folium
from folium.plugins import MarkerCluster
import os
import csv 
import time
import geopandas as gpd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import contextily as ctx


PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"



def load_data_calls(filename="dpd_calls_2025_features.csv"):
    """Read the feature-engineered dataset."""
    filepath = PROCESSED_DIR / filename
    df = pd.read_csv(filepath, parse_dates=['datetime'])

    # Recast dtypes lost on CSV round-trip
    for col in ['Nature', 'District', 'Disposition']:
        df[col] = df[col].astype('category')
    df['month'] = df['month'].astype('period[M]')

    return df

def load_API(API_KEY):
    """Loading API key."""
    load_dotenv()
    CARTO_API_KEY = os.getenv(API_KEY)
    if not CARTO_API_KEY:
        raise RuntimeError("CARTO_API_KEY not found")
    return CARTO_API_KEY

def long_lat(df, API_KEY):
    """Adding longitude and latitude features."""
    # Create GeoDataFrame using NC State Plane Feet (EPSG:2264)
    gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df['X'], df['Y']),
    crs='EPSG:2264'
    ).to_crs(epsg=3857)

    gdf_wgs84 = gdf.to_crs(epsg=4326)

    # Store converted values into clean columns
    df['longitude'] = gdf_wgs84.geometry.x
    df['latitude'] = gdf_wgs84.geometry.y

    # Returns validated df with new features longitude and latitude
    return df


def save_features_calls(df, filename="dpd_calls_2025_mapping_features.csv"):
    """Write the feature-engineered dataframe to PROCESSED_DIR."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / filename, index=False)
    return 

def main():
    df_calls = load_data_calls()
    df_calls = long_lat(df_calls, load_API("CARTO_API_KEY"))
    save_features_calls(df_calls)


if __name__ == "__main__":
    main()





"""

#1. finding local X, Y 
df_valid = df[
    (df['X'].between(1_900_000, 2_200_000)) &
    (df['Y'].between(700_000, 900_000))
].copy()

print(f"Dropped {len(df) - len(df_valid)} rows with invalid coordinates")

# 2. Create GeoDataFrame using NC State Plane Feet (EPSG:2264)
gdf = gpd.GeoDataFrame(
    df_valid,
    geometry=gpd.points_from_xy(df_valid['X'], df_valid['Y']),
    crs='EPSG:2264'
).to_crs(epsg=3857)

# 3. Transform points into global Longitude/Latitude degrees (EPSG:4326)
gdf_wgs84 = gdf.to_crs(epsg=4326)

# 4. Store converted values into clean columns
df_valid['longitude'] = gdf_wgs84.geometry.x
df_valid['latitude'] = gdf_wgs84.geometry.y

# 5. Save out the transformed file
df_valid.to_csv('police_data_latlon.csv', index=False)

"""