from typing import List
from collections import Counter


def unique_occurrences(arr: List[int]) -> bool:
    c = Counter(arr)
    return len(set(c.values())) == len(c.values())


print(unique_occurrences([1, 2, 2, 1, 1, 3]))
