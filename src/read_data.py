# src/read_data.py

import pandas as pd
import numpy as np
from src.create_grid import assign_grid_cells

def extract_first_lat_lon(link_points_str):

    try:
        points = link_points_str.split(' ')
        lat_str, lon_str = points[0].split(',')
        return float(lat_str), float(lon_str)
    except:
        return np.nan, np.nan

def load_and_clean_data(csv_path, grid_size=20):

    print("Loading CSV...")
    df = pd.read_csv(csv_path)

    df[['LAT', 'LON']] = df['LINK_POINTS'].apply(lambda x: pd.Series(extract_first_lat_lon(x)))
    df = df.dropna(subset=['LAT', 'LON', 'SPEED'])
    df = df[(df['SPEED'] >= 0) & (df['SPEED'] <= 100)]

    df = assign_grid_cells(df, grid_size=grid_size)

    print(f" Loaded and cleaned {len(df)} rows.")
    return df
