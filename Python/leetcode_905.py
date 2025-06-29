from typing import List


def sort_array_by_parity(nums: List[int]) -> List[int]:
    result: list[int] = []
    for num in nums:
        if num % 2 == 0:
            result.insert(0, num)
        else:
            result.append(num)
    return result
