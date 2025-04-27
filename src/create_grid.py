# src/create_grid.py

import numpy as np

def assign_grid_cells(df, grid_size=20):

    min_lat, max_lat = df['LAT'].min(), df['LAT'].max()
    min_lon, max_lon = df['LON'].min(), df['LON'].max()

    lat_edges = np.linspace(min_lat, max_lat, grid_size + 1)
    lon_edges = np.linspace(min_lon, max_lon, grid_size + 1)

    df['row'] = np.digitize(df['LAT'], lat_edges) - 1
    df['col'] = np.digitize(df['LON'], lon_edges) - 1

    df = df[
        (df['row'] >= 0) & (df['row'] < grid_size) &
        (df['col'] >= 0) & (df['col'] < grid_size)
    ]

    return df
