'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to\
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same\
character, but a character may map to itself.

I solved this problem firstly by checking if both strings are same length,\
then by checking if they have the same number of unique letters.
After that I created a dictionary where keys were s string characters and\
values were t string characters. Next I compared every s string values\
with t string values using dictionary, if even one letter mismatched\
it would mean that either the position or the letter was incorrect\
and the strings could not be isomophic.
'''


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if len(set(list(s))) != len(set(list(t))):
        return False
    s_dict = {}
    for i in range(len(s)):
        s_dict[s[i]] = t[i]
    for i in range(len(s)):
        if s_dict.get(s[i]) != t[i]:
            return False

    return True


print(is_isomorphic("bbbaaaba", "aaabbbba"))  # False
print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("paper", "title"))  # True
