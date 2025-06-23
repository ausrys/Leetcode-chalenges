from typing import List


def height_checker(heights: List[int]) -> int:
    sh = sorted(heights)
    result = 0
    for i, h in enumerate(sh):
        if h != heights[i]:
            result += 1
    return result
