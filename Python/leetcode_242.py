'''
Given two strings s and t, return true if t is an anagram of s
, and false otherwise.
'''


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # Assuming only lowercase letters

    for ch1, ch2 in zip(s, t):
        count[ord(ch1) - ord('a')] += 1
        count[ord(ch2) - ord('a')] -= 1

    return all(c == 0 for c in count)
