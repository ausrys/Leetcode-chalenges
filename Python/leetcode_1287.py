from collections import Counter
from typing import List


def find_special_integer(arr: List[int]) -> int:
    c = Counter(arr)
    return max(c, key=c.get)


print(find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]))
