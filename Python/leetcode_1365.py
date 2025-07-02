from typing import List


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    original = nums[:]
    nums.sort()
    nums.reverse()
    m = {}
    ln = len(nums)
    cn = 0
    for num in nums:
        cn += 1
        m[num] = ln - cn
    return [m[x] for x in original]


print(smaller_numbers_than_current([7, 7, 7, 7]))
