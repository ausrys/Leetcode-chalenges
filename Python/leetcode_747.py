'''
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as
much as every other number in the array. If it is, return the index of
the largest element, or return -1 otherwise.
'''
from typing import List


def dominant_index(nums: List[int]) -> int:
    sorted_arr = sorted(nums)
    max_num = sorted_arr[-1]
    if max_num >= sorted_arr[-2] * 2:
        return nums.index(max_num)
    return -1


print(dominant_index([1, 2, 3, 4]))
