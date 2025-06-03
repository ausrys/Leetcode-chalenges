'''
Return the number of different transformations
among all words we have.
'''

from typing import List


def unique_morse_representations(words: List[str]) -> int:
    letter_dict = {}
    seen_set: set[str] = set()
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
             ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
             "...-", ".--", "-..-", "-.--", "--.."]
    for index, morse_code in enumerate(morse):
        letter_dict[chr(index + 97)] = morse_code
    for word in words:
        morse_string = ''
        word_letter = list(word)
        for letter in word_letter:
            morse_string = morse_string + letter_dict[letter]
        seen_set.add(morse_string)
    return len(seen_set)


print(unique_morse_representations(["gin", "zen", "gig", "msg"]))
