'''
A sentence is a string of single-space separated words where each word
consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and
does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You
may return the answer in any order.
'''
from typing import List
from collections import Counter


def uncommon_from_sentences(s1: str, s2: str) -> List[str]:
    s1_c = Counter(s1.split())
    s2_c = Counter(s2.split())
    result = []
    for s in s1_c:
        if s1_c[s] == 1 and s not in s2_c:
            result.append(s)
    for s in s2_c:
        if s2_c[s] == 1 and s not in s1_c:
            result.append(s)
    return result


print(uncommon_from_sentences("this apple is sweet", "this apple is sour"))
