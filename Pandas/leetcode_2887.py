'''
Write a solution to fill in the missing value as 0 in the quantity column.
'''

import pandas as pd


def fill_missing_values(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
