'''
Given an integer n, return true if it is a power of three.
Otherwise, return false.

An integer n is a power of three, if there exists
an integer x such that n == 3x.

'''


def is_power_of_three(n: int) -> bool:
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1
