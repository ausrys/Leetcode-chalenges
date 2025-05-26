'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Fibonacci sequence
'''


def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1

    a, b = 1, 1  # a = ways(n-2), b = ways(n-1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(climb_stairs(3))  # 3
print(climb_stairs(4))  # 5
print(climb_stairs(5))  # 8
print(climb_stairs(6))  # 13
