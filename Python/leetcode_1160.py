from collections import Counter
from typing import List


def count_characters(words: List[str], chars: str) -> int:
    c = Counter(chars)
    result = 0
    for w in words:

        if c >= Counter(w):
            result += len(w)
    return result


print(count_characters(["cat", "bt", "hat", "tree"], "atach"))
