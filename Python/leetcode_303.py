'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right
inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of
nums between indices left and right inclusive (i.e. nums[left]
+ nums[left + 1] + ... + nums[right]).
'''

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.sum_arr = [0 for _ in range(N + 1)]
        for i in range(N):
            self.sum_arr[i + 1] = self.sum_arr[i] + nums[i]

    def sum_range(self, left: int, right: int) -> int:
        return self.sum_arr[right + 1] - self.sum_arr[left]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sum_arr)
print(obj.sum_range(2, 5))
