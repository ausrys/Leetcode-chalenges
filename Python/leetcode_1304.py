from typing import List


def sum_zero(n: int) -> List[int]:
    if n % 2 == 0:
        return list(range(-n + 1, n + 1, 2))
    return list(range(-n + 1, n, 2))
