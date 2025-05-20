import unittest


from leetcode_2891 import find_heavy_animals
from leetcode_2890 import melt_table
from leetcode_2889 import pivot_table
from leetcide_2888 import concat_tables
from leetcode_2887 import fill_missing_values
from leetcode_2886 import change_data_type
from leetcode_2885 import rename_columns
from leetcode_2884 import modify_salary_column
from leetcode_2883 import drop_missing_values
from leetcode_2882 import drop_duplicate_emails
from leetcode_2881 import create_bonus_column
from leetcode_2880 import select_data
from leetcode_2879 import select_first_rows
from leetcode_2877 import create_df
from leetcode_2878 import get_data_frame_size


import pandas as pd


# Unit test class


class TestDataFrameFunctions(unittest.TestCase):

    def test_empty_dataframe(self):
        df = pd.DataFrame()
        self.assertEqual(get_data_frame_size(df), [0, 0])

    def test_single_row_single_column(self):
        df = pd.DataFrame({'name': ['Alice']})
        self.assertEqual(get_data_frame_size(df), [1, 1])

    def test_multiple_rows_columns(self):
        data = {'name': ['Alice', 'Bob'], 'age': [30, 25]}
        df = pd.DataFrame(data)
        self.assertEqual(get_data_frame_size(df), [2, 2])

    def test_only_columns_no_rows(self):
        df = pd.DataFrame(columns=['name', 'age'])
        self.assertEqual(get_data_frame_size(df), [0, 2])

    def test_only_rows_no_columns(self):
        df = pd.DataFrame(index=[0, 1])
        self.assertEqual(get_data_frame_size(df), [2, 0])

    # Tests for create_df

    def test_create_df_empty(self):
        df = create_df([])
        self.assertTrue(df.empty)
        self.assertListEqual(list(df.columns), ['student_id', 'age'])
        self.assertEqual(get_data_frame_size(df), [0, 2])

    def test_create_df_single_entry(self):
        df = create_df([[1, 20]])
        self.assertEqual(get_data_frame_size(df), [1, 2])
        self.assertEqual(df.iloc[0]['student_id'], 1)
        self.assertEqual(df.iloc[0]['age'], 20)

    # Tests for select_first_rows

    def test_create_df_multiple_entries(self):
        data = [[1, 20], [2, 22], [3, 19]]
        df = create_df(data)
        self.assertEqual(get_data_frame_size(df), [3, 2])
        self.assertListEqual(df['student_id'].tolist(), [1, 2, 3])
        self.assertListEqual(df['age'].tolist(), [20, 22, 19])

    def test_select_first_rows_less_than_3(self):
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})
        result = select_first_rows(df)
        self.assertEqual(len(result), 2)
        self.assertListEqual(result['name'].tolist(), ['Alice', 'Bob'])

    def test_select_first_rows_exactly_3(self):
        df = pd.DataFrame(
            {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 28]})
        result = select_first_rows(df)
        self.assertEqual(len(result), 3)
        self.assertListEqual(result['name'].tolist(), [
                             'Alice', 'Bob', 'Charlie'])

    def test_select_first_rows_more_than_3(self):
        df = pd.DataFrame(
            {'name': ['Alice', 'Bob', 'Charlie', 'David'],
             'age': [30, 25, 28, 40]})
        result = select_first_rows(df)
        self.assertEqual(len(result), 3)
        self.assertListEqual(result['name'].tolist(), [
                             'Alice', 'Bob', 'Charlie'])

    def test_select_first_rows_empty_df(self):
        df = pd.DataFrame(columns=['name', 'age'])
        result = select_first_rows(df)
        self.assertTrue(result.empty)

        # Tests for select_data
    def test_select_data_matching_id(self):
        df = pd.DataFrame({
            'student_id': [101, 102, 101],
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [20, 21, 22]
        })
        result = select_data(df)
        self.assertEqual(len(result), 2)
        self.assertListEqual(result['name'].tolist(), ['Alice', 'Charlie'])
        self.assertListEqual(result['age'].tolist(), [20, 22])
        self.assertListEqual(list(result.columns), ['name', 'age'])

    def test_select_data_no_match(self):
        df = pd.DataFrame({
            'student_id': [102, 103],
            'name': ['Bob', 'Dave'],
            'age': [21, 23]
        })
        result = select_data(df)
        self.assertTrue(result.empty)
        self.assertListEqual(list(result.columns), ['name', 'age'])

    def test_select_data_empty_df(self):
        df = pd.DataFrame(columns=['student_id', 'name', 'age'])
        result = select_data(df)
        self.assertTrue(result.empty)
        self.assertListEqual(list(result.columns), ['name', 'age'])

        # Tests for create_bonus_column
    def test_create_bonus_column_normal(self):
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'salary': [1000, 1500]})
        result = create_bonus_column(df.copy())
        self.assertIn('bonus', result.columns)
        self.assertListEqual(result['bonus'].tolist(), [2000, 3000])

    def test_create_bonus_column_zero_salary(self):
        df = pd.DataFrame({'name': ['Alice'], 'salary': [0]})
        result = create_bonus_column(df.copy())
        self.assertEqual(result['bonus'].iloc[0], 0)

    def test_create_bonus_column_negative_salary(self):
        df = pd.DataFrame({'name': ['Bob'], 'salary': [-500]})
        result = create_bonus_column(df.copy())
        self.assertEqual(result['bonus'].iloc[0], -1000)

    def test_create_bonus_column_empty_df(self):
        df = pd.DataFrame(columns=['name', 'salary'])
        result = create_bonus_column(df.copy())
        self.assertIn('bonus', result.columns)
        self.assertTrue(result.empty)

        # Tests for drop_duplicate_emails
    def test_drop_duplicate_emails_some_duplicates(self):
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie'],
            'email': ['a@example.com', 'b@example.com', 'a@example.com']
        })
        result = drop_duplicate_emails(df)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result['email'].unique()), 2)

    def test_drop_duplicate_emails_no_duplicates(self):
        df = pd.DataFrame({
            'name': ['Alice', 'Bob'],
            'email': ['a@example.com', 'b@example.com']
        })
        result = drop_duplicate_emails(df)
        self.assertEqual(len(result), 2)
        self.assertListEqual(result['email'].tolist(), [
                             'a@example.com', 'b@example.com'])

    def test_drop_duplicate_emails_all_duplicates(self):
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie'],
            'email': ['a@example.com', 'a@example.com', 'a@example.com']
        })
        result = drop_duplicate_emails(df)
        self.assertEqual(len(result), 1)
        self.assertEqual(result['email'].iloc[0], 'a@example.com')

    def test_drop_duplicate_emails_empty_df(self):
        df = pd.DataFrame(columns=['name', 'email'])
        result = drop_duplicate_emails(df)
        self.assertTrue(result.empty)
        self.assertListEqual(list(result.columns), ['name', 'email'])

        # Tests for drop_missing_values
    def test_drop_missing_values_some_missing(self):
        df = pd.DataFrame({
            'student_id': [101, 102, 103],
            'name': ['Alice', None, 'Charlie'],
            'age': [20, 21, 22]
        })
        result = drop_missing_values(df)
        self.assertEqual(len(result), 2)
        self.assertNotIn(None, result['name'].values)

    def test_drop_missing_values_no_missing(self):
        df = pd.DataFrame({
            'student_id': [101, 102],
            'name': ['Alice', 'Bob'],
            'age': [20, 21]
        })
        result = drop_missing_values(df)
        self.assertEqual(len(result), 2)

    def test_drop_missing_values_all_missing(self):
        df = pd.DataFrame({
            'student_id': [101, 102],
            'name': [None, None],
            'age': [20, 21]
        })
        result = drop_missing_values(df)
        self.assertTrue(result.empty)

    def test_drop_missing_values_empty_df(self):
        df = pd.DataFrame(columns=['student_id', 'name', 'age'])
        result = drop_missing_values(df)
        self.assertTrue(result.empty)
        self.assertListEqual(list(result.columns), [
                             'student_id', 'name', 'age'])

    # Tests for modify_salary_column
    def test_modify_salary_column_normal(self):
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'salary': [1000, 1500]})
        result = modify_salary_column(df.copy())
        self.assertListEqual(result['salary'].tolist(), [2000, 3000])

    def test_modify_salary_column_zero_salary(self):
        df = pd.DataFrame({'name': ['Alice'], 'salary': [0]})
        result = modify_salary_column(df.copy())
        self.assertEqual(result['salary'].iloc[0], 0)

    def test_modify_salary_column_negative_salary(self):
        df = pd.DataFrame({'name': ['Bob'], 'salary': [-500]})
        result = modify_salary_column(df.copy())
        self.assertEqual(result['salary'].iloc[0], -1000)

    def test_modify_salary_column_empty_df(self):
        df = pd.DataFrame(columns=['name', 'salary'])
        result = modify_salary_column(df.copy())
        self.assertTrue(result.empty)
        self.assertIn('salary', result.columns)

        # Tests for rename_columns
    def test_rename_columns_all_present(self):
        df = pd.DataFrame({
            'id': [1, 2],
            'first': ['Alice', 'Bob'],
            'last': ['Smith', 'Jones'],
            'age': [20, 21]
        })
        result = rename_columns(df)
        self.assertListEqual(
            sorted(result.columns.tolist()),
            sorted(['student_id', 'first_name', 'last_name', 'age_in_years'])
        )
        self.assertListEqual(result['student_id'].tolist(), [1, 2])
        self.assertListEqual(result['first_name'].tolist(), ['Alice', 'Bob'])

    def test_rename_columns_some_missing(self):
        df = pd.DataFrame({
            'id': [1],
            'first': ['Alice'],
            'age': [20]
        })
        result = rename_columns(df)
        self.assertIn('student_id', result.columns)
        self.assertIn('first_name', result.columns)
        self.assertIn('age_in_years', result.columns)
        self.assertNotIn('last_name', result.columns)

    def test_rename_columns_no_matching_columns(self):
        df = pd.DataFrame({
            'student_no': [1],
            'name': ['Alice']
        })
        result = rename_columns(df)
        self.assertListEqual(result.columns.tolist(), ['student_no', 'name'])

    def test_rename_columns_empty_df(self):
        df = pd.DataFrame()
        result = rename_columns(df)
        self.assertTrue(result.empty)

        # Tests for change_data_type
    def test_change_data_type_normal(self):
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'grade': [90.0, 85.5]})
        result = change_data_type(df.copy())
        self.assertTrue(pd.api.types.is_integer_dtype(result['grade']))
        self.assertListEqual(result['grade'].tolist(), [90, 85])

    def test_change_data_type_already_int(self):
        df = pd.DataFrame({'name': ['Alice'], 'grade': [75]})
        result = change_data_type(df.copy())
        self.assertTrue(pd.api.types.is_integer_dtype(result['grade']))
        self.assertEqual(result['grade'].iloc[0], 75)

    def test_change_data_type_with_strings(self):
        df = pd.DataFrame({'name': ['Alice'], 'grade': ['100']})
        result = change_data_type(df.copy())
        self.assertTrue(pd.api.types.is_integer_dtype(result['grade']))
        self.assertEqual(result['grade'].iloc[0], 100)

    def test_change_data_type_empty_df(self):
        df = pd.DataFrame(columns=['name', 'grade'])
        result = change_data_type(df.copy())
        self.assertTrue(result.empty)
        self.assertIn('grade', result.columns)

        # Tests for fill_missing_values
    def test_fill_missing_values_some_missing(self):
        df = pd.DataFrame({
            'product': ['A', 'B', 'C'],
            'quantity': [10, None, 5]
        })
        result = fill_missing_values(df.copy())
        self.assertListEqual(result['quantity'].tolist(), [10, 0, 5])

    def test_fill_missing_values_all_missing(self):
        df = pd.DataFrame({
            'product': ['A', 'B'],
            'quantity': [None, None]
        })
        result = fill_missing_values(df.copy())
        self.assertListEqual(result['quantity'].tolist(), [0, 0])

    def test_fill_missing_values_no_missing(self):
        df = pd.DataFrame({
            'product': ['A', 'B'],
            'quantity': [3, 7]
        })
        result = fill_missing_values(df.copy())
        self.assertListEqual(result['quantity'].tolist(), [3, 7])

    def test_fill_missing_values_empty_df(self):
        df = pd.DataFrame(columns=['product', 'quantity'])
        result = fill_missing_values(df.copy())
        self.assertTrue(result.empty)
        self.assertIn('quantity', result.columns)

        # Tests for concat_tables
    def test_concat_tables_same_columns(self):
        df1 = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
        df2 = pd.DataFrame({'id': [3], 'name': ['Charlie']})
        result = concat_tables(df1, df2)
        self.assertEqual(len(result), 3)
        self.assertListEqual(result['id'].tolist(), [1, 2, 3])
        self.assertListEqual(result['name'].tolist(), [
                             'Alice', 'Bob', 'Charlie'])

    def test_concat_tables_different_columns(self):
        df1 = pd.DataFrame({'id': [1], 'name': ['Alice']})
        df2 = pd.DataFrame({'id': [2], 'age': [30]})
        result = concat_tables(df1, df2)
        self.assertEqual(len(result), 2)
        self.assertIn('name', result.columns)
        self.assertIn('age', result.columns)
        self.assertTrue(pd.isna(result.iloc[1]['name']))
        self.assertTrue(pd.isna(result.iloc[0]['age']))

    def test_concat_tables_one_empty(self):
        df1 = pd.DataFrame({'id': [1], 'name': ['Alice']})
        df2 = pd.DataFrame(columns=['id', 'name'])
        result = concat_tables(df1, df2)
        self.assertEqual(len(result), 1)
        self.assertListEqual(result['name'].tolist(), ['Alice'])

    def test_concat_tables_both_empty(self):
        df1 = pd.DataFrame(columns=['id', 'name'])
        df2 = pd.DataFrame(columns=['id', 'name'])
        result = concat_tables(df1, df2)
        self.assertTrue(result.empty)
        self.assertListEqual(list(result.columns), ['id', 'name'])

        # Tests for pivot_table
    def test_pivot_table_normal(self):
        df = pd.DataFrame({
            'month': ['Jan', 'Jan', 'Feb', 'Feb'],
            'city': ['NY', 'LA', 'NY', 'LA'],
            'temperature': [30, 60, 32, 62]
        })
        result = pivot_table(df)
        self.assertEqual(result.loc['Jan', 'NY'], 30)
        self.assertEqual(result.loc['Feb', 'LA'], 62)
        self.assertListEqual(sorted(result.columns.tolist()), ['LA', 'NY'])
        self.assertListEqual(sorted(result.index.tolist()), ['Feb', 'Jan'])

    def test_pivot_table_missing_data(self):
        df = pd.DataFrame({
            'month': ['Jan', 'Feb'],
            'city': ['NY', 'LA'],
            'temperature': [30, 60]
        })
        result = pivot_table(df)
        self.assertTrue(pd.isna(result.loc['Jan', 'LA']))
        self.assertEqual(result.loc['Feb', 'LA'], 60)

    def test_pivot_table_single_entry(self):
        df = pd.DataFrame({
            'month': ['Jan'],
            'city': ['NY'],
            'temperature': [25]
        })
        result = pivot_table(df)
        self.assertEqual(result.loc['Jan', 'NY'], 25)

    def test_pivot_table_empty_df(self):
        df = pd.DataFrame(columns=['month', 'city', 'temperature'])
        result = pivot_table(df)
        self.assertTrue(result.empty)

        # Tests for melt_table
    def test_melt_table_normal(self):
        df = pd.DataFrame({
            'product': ['A', 'B'],
            'quarter_1': [100, 200],
            'quarter_2': [150, 250],
            'quarter_3': [200, 300],
            'quarter_4': [250, 350]
        })
        result = melt_table(df)
        self.assertEqual(len(result), 8)
        self.assertIn('product', result.columns)
        self.assertIn('quarter', result.columns)
        self.assertIn('sales', result.columns)
        self.assertEqual(result[result['product'] == 'A']
                         ['sales'].tolist(), [100, 150, 200, 250])

    def test_melt_table_missing_sales(self):
        df = pd.DataFrame({
            'product': ['A'],
            'quarter_1': [None],
            'quarter_2': [150],
            'quarter_3': [None],
            'quarter_4': [250]
        })
        result = melt_table(df)
        self.assertEqual(len(result), 4)
        self.assertTrue(pd.isna(result.iloc[0]['sales']))
        self.assertEqual(result.iloc[1]['sales'], 150)

    def test_melt_table_single_product(self):
        df = pd.DataFrame({
            'product': ['A'],
            'quarter_1': [10],
            'quarter_2': [20],
            'quarter_3': [30],
            'quarter_4': [40]
        })
        result = melt_table(df)
        self.assertListEqual(result['sales'].tolist(), [10, 20, 30, 40])
        self.assertListEqual(result['quarter'].tolist(), [
                             'quarter_1', 'quarter_2', 'quarter_3',
                             'quarter_4'])

    def test_melt_table_empty_df(self):
        df = pd.DataFrame(
            columns=['product', 'quarter_1', 'quarter_2', 'quarter_3',
                     'quarter_4'])
        result = melt_table(df)
        self.assertTrue(result.empty)
        self.assertListEqual(result.columns.tolist(), [
                             'product', 'quarter', 'sales'])

        # Tests for find_heavy_animals
    def test_find_heavy_animals_normal(self):
        df = pd.DataFrame({
            'name': ['Elephant', 'Dog', 'Horse', 'Cat'],
            'weight': [5000, 30, 400, 10]
        })
        result = find_heavy_animals(df)
        self.assertListEqual(result['name'].tolist(), ['Elephant', 'Horse'])

    def test_find_heavy_animals_all_light(self):
        df = pd.DataFrame({
            'name': ['Rabbit', 'Cat'],
            'weight': [5, 10]
        })
        result = find_heavy_animals(df)
        self.assertTrue(result.empty)

    def test_find_heavy_animals_all_heavy(self):
        df = pd.DataFrame({
            'name': ['Rhino', 'Hippo'],
            'weight': [2000, 1500]
        })
        result = find_heavy_animals(df)
        self.assertListEqual(result['name'].tolist(), ['Rhino', 'Hippo'])

    def test_find_heavy_animals_exactly_100(self):
        df = pd.DataFrame({
            'name': ['Crocodile', 'Alligator'],
            'weight': [100, 150]
        })
        result = find_heavy_animals(df)
        self.assertListEqual(result['name'].tolist(), ['Alligator'])

    def test_find_heavy_animals_empty_df(self):
        df = pd.DataFrame(columns=['name', 'weight'])
        result = find_heavy_animals(df)
        self.assertTrue(result.empty)
        self.assertListEqual(result.columns.tolist(), ['name'])


if __name__ == '__main__':
    unittest.main()
