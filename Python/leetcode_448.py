'''
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear
in nums.
'''
from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    s = set(nums)
    return [i for i in range(1, len(nums)+1) if i not in s]
