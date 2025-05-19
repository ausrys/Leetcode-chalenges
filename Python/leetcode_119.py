'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above

'''
from typing import List


def get_row(row_index: int) -> List[int]:
    result: List[List[int]] = []
    for i in range(row_index):
        row = [1] * (i + 1)  # Initialize row with 1s
        for j in range(1, i):  # Fill the middle elements
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)

    return result[-1]


print(get_row(0))
