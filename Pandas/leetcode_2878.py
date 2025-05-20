'''
Write a solution to calculate and display the number
of rows and columns of players.
'''
from typing import List
import pandas as pd


def get_data_frame_size(players: pd.DataFrame) -> List[int]:
    return [len(players.index), len(players.columns)]


# Faster solution list(players.shape)
