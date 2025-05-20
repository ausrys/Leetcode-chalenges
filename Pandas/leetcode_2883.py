'''
There are some rows having missing values in the name column.

Write a solution to remove the rows with missing values.
'''
import pandas as pd


def drop_missing_values(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='name')
