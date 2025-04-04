'''
Given two strings needle and haystack, return the index of the first\
occurrence of needle in haystack, or -1 if needle is not part of haystack.

We check if provided needle exists in haystack and then check its index.
'''


def str_check(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1


print(str_check("asdasdaleetcode", "zleet"))  # -1

print(str_check("asasdasdaleetcoded", "leet"))  # 9
