import numpy as np
import pandas as pd


def log_plus_one(x):
    return np.log(x + 1)


def log_columns(df: pd.DataFrame, cols: [str]):
    for c in cols:
        df[c] = df[c].apply(log_plus_one)
    df.rename(columns={c: f"l_{c}" for c in cols}, inplace=True)
