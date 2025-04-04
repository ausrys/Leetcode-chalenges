'''
Given a string s consisting of words and spaces, return the length of the last\
word in the string.
A word is a maximal substring consisting of non-space characters only.

I aproached this problem by splitting into the array and then checked last\
member's length.
'''


def length_of_last_word(s: str) -> int:
    arr = s.split()
    return len(arr[-1])


print(length_of_last_word("Hello World"))  # output 5
print(length_of_last_word("   fly me   to   the moon  "))  # output 4
