'''
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

We clean the string and compare cleaned to it reversed.
'''


def is_palindrome(s: str):
    cleaned = ''.join(c for c in s if c.isalnum()).lower()
    return cleaned == cleaned[::-1]


print(is_palindrome("aabbaa"))  # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # true
