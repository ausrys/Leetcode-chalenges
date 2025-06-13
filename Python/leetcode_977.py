'''
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
'''
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result.append(nums[right] ** 2)
            right -= 1
        else:
            result.append(nums[left] ** 2)
            left += 1
    return result[::-1]
