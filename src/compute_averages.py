# src/compute_averages.py

import numpy as np
import pandas as pd

def compute_hourly_averages(df, grid_size=10):
    grouped = df.groupby(['HOUR', 'row', 'col'])['SPEED'].mean().reset_index()

    hourly_grids = {hour: np.full((grid_size, grid_size), np.nan) for hour in range(24)}

    for _, row in grouped.iterrows():
        hour = int(row['HOUR'])
        r, c = int(row['row']), int(row['col'])
        hourly_grids[hour][r, c] = row['SPEED']

    return hourly_grids
