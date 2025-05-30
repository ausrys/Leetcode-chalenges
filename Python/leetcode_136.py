'''
Given a non-empty array of integers nums, every element
appears twice except for one. Find that single one.

You must implement a solution with a linear runtime
complexity and use only constant extra space.
'''
from typing import List


def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR accumulates the unique number
    return result
