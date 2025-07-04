from collections import Counter
from typing import List


def find_lhs(nums: List[int]) -> int:
    c = Counter(nums)
    max_l = 0
    for n in c:
        if n+1 in c:
            max_l = max(max_l, c[n] + c[n+1])
    return max_l


print(find_lhs([1, 3, 5, 4, 5, 2, 3, 7]))
