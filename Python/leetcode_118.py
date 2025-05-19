'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above.
'''


from typing import List


def generate(num_rows: int) -> List[List[int]]:
    result: List[List[int]] = []

    for i in range(num_rows):
        row = [1] * (i + 1)  # Initialize row with 1s
        for j in range(1, i):  # Fill the middle elements
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)

    return result


print(generate(5))
