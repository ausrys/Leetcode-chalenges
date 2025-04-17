'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.
'''


def reverse_vowels(s: str) -> str:
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowels_in_string: list = []
    string_list = list(s)
    x = 0
    for char in s:
        if char in vowels_set:
            vowels_in_string.append(char)
    vowels_in_string.reverse()
    for i, char in enumerate(string_list):
        if char in vowels_set:
            string_list[i] = vowels_in_string[x]
            x += 1
    return ''.join(string_list)


print(reverse_vowels("IceCreAm"))
