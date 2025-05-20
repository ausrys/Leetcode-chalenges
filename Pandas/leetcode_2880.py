'''
Write a solution to select the name and age of the student with
student_id = 101.
'''

import pandas as pd


def select_data(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]
