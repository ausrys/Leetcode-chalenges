from collections import Counter


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    stones_counter = Counter(stones)
    result = 0
    for j in jewels:
        if j in stones_counter:
            result += stones_counter[j]
    return result
