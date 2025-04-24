'''
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    ransom_counter = Counter(ransom_note)
    magazine_counter = Counter(magazine)

    for char, count in ransom_counter.items():
        if magazine_counter[char] < count:
            return False
    return True


print(can_construct("aa", "baa"))
