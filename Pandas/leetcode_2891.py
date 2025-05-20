'''
Write a solution to list the names of animals that weigh
strictly more than 100 kilograms.
'''

import pandas as pd


def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    result = animals[animals['weight'] > 100] \
        .sort_values(by='weight', ascending=False)[['name']]
    return result
