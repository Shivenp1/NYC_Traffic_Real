# main.py

import pandas as pd
from src.create_grid import assign_grid_cells
from src.compute_averages import compute_hourly_averages
from src.plot_heatmap import grid_to_lat_lon_points, plot_heatmap_on_map
from src.read_data import load_and_clean_data

def main():
    df = load_and_clean_data('data/Midtown_traffic.csv', grid_size=20)

    df['HOUR'] = pd.to_datetime(df['DATA_AS_OF']).dt.hour

    lat_min = df['LAT'].min()
    lat_max = df['LAT'].max()
    lon_min = df['LON'].min()
    lon_max = df['LON'].max()

    hourly_grids = compute_hourly_averages(df, grid_size=20)

    all_points = []


    for hour in range(24):
        grid = hourly_grids[hour]

        points_df = grid_to_lat_lon_points(grid, lat_min, lat_max, lon_min, lon_max, grid_size=20)

        points_df['HOUR'] = hour

        all_points.append(points_df)

    final_points_df = pd.concat(all_points, ignore_index=True)

    plot_heatmap_on_map(final_points_df)

if __name__ == "__main__":
    main()
