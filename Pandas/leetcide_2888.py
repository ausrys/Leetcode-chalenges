'''
Write a solution to concatenate these two DataFrames
vertically into one DataFrame.
'''
import pandas as pd


def concat_tables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df1, df2])
    return df
