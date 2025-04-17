'''
Write a function that reverses a string. The input string is given as an array
of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''


def reverse_string(s: list):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    s.reverse()


print(reverse_string(["H", "a", "n", "n", "a", "h"]))
