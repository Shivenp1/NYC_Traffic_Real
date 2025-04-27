import plotly.express as px
import numpy as np
import pandas as pd

def row_col_to_lat_lon(row, col, lat_min, lat_max, lon_min, lon_max, grid_size=20):
   
    lat_step = (lat_max - lat_min) / grid_size
    lon_step = (lon_max - lon_min) / grid_size

    lat = lat_min + (row + 0.5) * lat_step
    lon = lon_min + (col + 0.5) * lon_step

    return lat, lon

def grid_to_lat_lon_points(grid, lat_min, lat_max, lon_min, lon_max, grid_size=20):
    
    points = []

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            speed = grid[row, col]
            if not np.isnan(speed) and speed > 0:
                lat, lon = row_col_to_lat_lon(row, col, lat_min, lat_max, lon_min, lon_max, grid_size)
                points.append((lat, lon, speed))

    return pd.DataFrame(points, columns=['LAT', 'LON', 'SPEED'])

def plot_heatmap_on_map(points_df):

    fig = px.scatter_mapbox(
        points_df,
        lat="LAT",
        lon="LON",
        color="SPEED",
        color_continuous_scale="Viridis",
        range_color=(0, 40),
        size=[20]*len(points_df),
        size_max=30,
        zoom=13,
        center={"lat": 40.71, "lon": -73.99},
        mapbox_style="open-street-map",
        animation_frame="HOUR" 
    )

    fig.update_layout(
        title="Animated Traffic Speeds (Downtown Manhattan & Brooklyn)",
        margin={"r":0,"t":30,"l":0,"b":0},
        updatemenus=[{
            "buttons": [
                {"args": [None, {"frame": {"duration": 1000, "redraw": True}, "fromcurrent": True}],
                 "label": "Play",
                 "method": "animate"},
                {"args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                 "label": "Pause",
                 "method": "animate"}
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 70},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }],
        sliders=[{
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Hour: ",
                "visible": True,
                "xanchor": "right"
            },
            "transition": {"duration": 300, "easing": "cubic-in-out"},
            "pad": {"b": 10, "t": 50},
            "len": 0.9,
            "x": 0.1,
            "y": 0,
        }]
    )

    fig.show()
