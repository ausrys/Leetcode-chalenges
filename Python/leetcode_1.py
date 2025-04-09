'''
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
'''

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store the number and its index
    num_map: dict = {}

    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # If the complement exists in the map, we've found the solution
        if complement in num_map:
            return [num_map[complement], i]

        # Otherwise, store the current number and its index in the map
        num_map[num] = i

    return []
