'''
Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
In this problem I converted the number into the string and
reversed the string. Then I compared both strings to see if they are equal
'''


def isPalindrome(x: int) -> bool:
    if str(x) != (str(x)[::-1]):
        return False

    return True


print(isPalindrome(212))  # True
print(isPalindrome(213))  # False
print(isPalindrome(-212))  # False
