from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []

    def backtrack(path: List, used: set):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in nums:
            if i in used:
                continue
            path.append(i)
            used.add(i)
            backtrack(path, used)
            path.pop()
            used.remove(i)
    backtrack([], set())

    return result
