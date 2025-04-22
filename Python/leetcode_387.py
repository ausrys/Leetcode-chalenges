'''
Given a string s, find the first non-repeating character in it and return
its index. If it does not exist, return -1.

First we make a dictionary of characters and their repeat count.
Then we find first one which has repeated 1 time and returns its index
'''


def first_uniq_char(s: str) -> int:
    chars = {}
    for char in s:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] = chars[char] + 1
    for key, value in chars.items():
        if value == 1:
            return s.index(str(key))
    return -1


print(first_uniq_char("leetcode"))
print(first_uniq_char("loveleetcode"))
print(first_uniq_char("aabb"))
