'''
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and you may
return the result in any order.

Return intersection of 2 sets
'''

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:

    return [x for x in set(nums1) & set(nums2)]


print(intersection([1, 2, 2, 1], [2, 2]))
