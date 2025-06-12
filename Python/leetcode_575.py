from typing import List


def distribute_candies(candyType: List[int]) -> int:
    sn = len(set(candyType))
    n = len(candyType) // 2
    if n >= sn:
        return sn
    return n
