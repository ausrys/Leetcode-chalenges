'''
Reverse the 32 bits of a given integer and return it as an integer.
'''


def reverse_bits(n: int) -> int:
    binary_32_bit = format(n, '032b')
    reversed_string = str(binary_32_bit[::-1])
    return int(reversed_string, 2)


print(reverse_bits(5))
