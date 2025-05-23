'''
Write a solution to reshape the data so that each row
represents sales data for a product in a specific quarter.
'''
import pandas as pd


def melt_table(report: pd.DataFrame) -> pd.DataFrame:
    reshaped_df = report.melt(id_vars='product',
                              value_vars=['quarter_1', 'quarter_2',
                                          'quarter_3', 'quarter_4'],
                              var_name='quarter',
                              value_name='sales')
    return reshaped_df
