from typing import List


def array_pair_sum(nums: List[int]) -> int:
    nums.sort()
    final_sum = 0
    for i in range(0, len(nums) - 1, 2):
        final_sum += min(nums[i], nums[i+1])
    return final_sum


print(array_pair_sum([1, 4, 3, 2]))
