'''
There are some duplicate rows in the DataFrame based on the
email column.

Write a solution to remove these duplicate rows and keep
only the first occurrence.
'''

import pandas as pd


def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email')
