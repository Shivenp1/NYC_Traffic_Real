import pandas as pd

def fetch_live_data():
    """
    Loads local Midtown traffic CSV.
    """
    df = pd.read_csv('data/Midtown_traffic.csv')
    return df
