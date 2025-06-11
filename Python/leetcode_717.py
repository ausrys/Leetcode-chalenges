from typing import List


def is_one_bit_character(bits: List[int]) -> bool:
    i = 0
    while i < len(bits) - 1:
        if bits[i] == 0:
            i += 1
        elif bits[i] == 1:
            i += 2
    return i == len(bits) - 1


print(is_one_bit_character([0, 1, 0]))
