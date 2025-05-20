'''
A company intends to give its employees a pay rise.

Write a solution to modify the salary column by
multiplying each salary by 2.
'''
import pandas as pd


def modify_salary_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
