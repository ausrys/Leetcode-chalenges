from collections import Counter
from typing import List


def common_chars(words: List[str]) -> List[str]:
    common = Counter(words[0])

    for word in words[1:]:
        common &= Counter(word)  # intersection: min counts

    result = []
    for char, freq in common.items():
        result.extend([char] * freq)

    return result


print(common_chars(["cool", "lock", "cook"]))
