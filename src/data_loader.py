# src/data_loader.py
import pandas as pd

def load_data(path="data/raw/MapProjects_data.csv"):
    df = pd.read_csv(path)
    return df
