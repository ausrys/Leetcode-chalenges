'''
You are given an integer array nums. You need to ensure that the elements in
the array are distinct. To achieve this, you can perform the following
operation any number of times:

Remove 3 elements from the beginning of the array. If the array has fewer than
3 elements, remove all remaining elements.
Note that an empty array is considered to have distinct elements.
Return the minimum number of operations needed to make the elements in the
array distinct.

This problem was solved by doing while loop as long as there is a list
and checking if the list contains only unique items, if not
we slice the list. we take out first 3 numbers.
'''

from typing import List


def minimum_operations(nums: List[int]) -> int:
    operations: int = 0
    while len(nums) > 0:
        if len(nums) == len(set(nums)):
            return operations
        nums = nums[3:]

        operations += 1
    return operations


print(minimum_operations([4, 5, 6, 4, 4]))  # output 2
print(minimum_operations([3, 7, 12, 12, 3, 14, 1, 1]))  # output 3
