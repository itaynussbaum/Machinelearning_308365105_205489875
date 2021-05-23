import pandas as pd
import numpy as np


def clean_file(df):
    df.rename(columns={0: "id"},  inplace=True)
    return df


df = pd.read_csv("./feature_data.csv")
clean_file(df)
print(df)
