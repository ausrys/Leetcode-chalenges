'''
Given an integer array nums and an integer k, return true if there are two\
distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    index_map: dict[int, int] = {}  # Stores value: last_seen_index

    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i  # Update the last seen index
    return False
