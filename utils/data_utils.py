# utils/data_utils.py
import pandas as pd

def load_csv(file_name):
    return pd.read_csv(file_name)

def save_csv(data, file_name):
    data.to_csv(file_name, index=False)