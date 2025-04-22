'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding
ones, starting from 0 and 1. That is,
'''


def fib(n):
    if n <= 1:
        return n
    # Compute and cache the Fibonacci value
    return fib(n - 1) + fib(n - 2)


print(fib(6))
