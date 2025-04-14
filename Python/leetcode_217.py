'''
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element
is distinct.

We just return the result of comparison of lengths between
original array and that array converted to set.
'''
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False
