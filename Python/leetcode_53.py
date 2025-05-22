from typing import List
# Given an integer array nums, find the subarray with the largest sum,
# and return its sum.


def max_sub_array(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, 0)
    return int(max_sum)
