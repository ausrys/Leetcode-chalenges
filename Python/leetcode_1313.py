from typing import List


def decompress_rle_list(nums: List[int]) -> List[int]:
    result = []
    for i in range(0, len(nums) - 1, 2):
        result.extend([nums[i+1]] * nums[i])
    return result


print(decompress_rle_list([1, 1, 2, 3]))
