'''
Given a string licensePlate and an array of strings words, find the shortest
completing word in words.

A completing word is a word that contains all the letters in licensePlate.
Ignore numbers and spaces in licensePlate, and treat letters as case
insensitive.
If a letter appears more than once in licensePlate, then it must appear in the
word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b'
(ignoring case), and 'c' twice. Possible completing words are "abccdef",
"caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer
exists. If there are multiple shortest completing words, return the first
one that occurs in words.
'''
from typing import List
import re
from collections import Counter


def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
    cleaned = list(re.sub(r"[0-9\s]+", "", licensePlate).lower())
    main_counter = Counter(cleaned)
    min_word = None

    for word in words:
        word_counter = Counter(word)
        if all(word_counter[char] >= main_counter[char] for char
               in main_counter):
            if min_word is None or len(word) < len(min_word):
                min_word = word

    return min_word


print(shortestCompletingWord("iLMOl80", [
      "send", "why", "want", "program", "million", "wonder", "manager",
      "success", "likely", "them"]))
