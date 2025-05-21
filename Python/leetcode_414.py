'''
Given an integer array nums, return the third distinct maximum number in
this array. If the third maximum does not exist, return the maximum number.
'''
from typing import List


def third_max(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    uniques = list(set(nums))
    uniques.sort()
    if len(uniques) >= 3:
        return uniques[-3]
    return uniques[-1]
