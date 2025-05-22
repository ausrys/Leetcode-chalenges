'''
Given a binary array nums, return the maximum number
of consecutive 1's in the array.
'''


from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    max_number = 0
    temp_number = 0
    for num in nums:
        if num == 1:
            temp_number += 1
            max_number = max(max_number, temp_number)
        else:
            temp_number = 0
    return max_number
