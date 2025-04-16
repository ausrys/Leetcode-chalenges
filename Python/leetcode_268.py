'''
Given an array nums containing n distinct numbers in the range [0, n],
sreturn the only number in the range that is missing from the array.

I sort the array in the ascending order and then search the missing
number by comparind index with the number there should be
'''

from typing import List


def missing_number(nums: List[int]) -> int:
    nums.sort()
    for i, num in enumerate(nums):
        if i != num:
            return i

    return len(nums)


print(missing_number([1, 2]))  # 0
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
print(missing_number([0, 1]))  # 2
