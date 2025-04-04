'''
 Check If a Word Occurs As a Prefix of Any Word in a Sentence
 Given a sentence that consists of some words separated by a single space, and\
 a searchWord, check if searchWord is a prefix of any word in sentence.

 Return the index of the word in sentence (1-indexed) where searchWord is a\
 prefix of this word. If searchWord is a prefix of more than one word, return \
 the index of the first word (minimum index).
 If there is no such word return -1.
 In this challenge I decided to extract the words from the string in to the\
 list and then loop through the list searching for a word that starts with \
 provided prefix. If the program finds the word, it returs the variable i\
 which represents the position of word in a string. If the program does not \
 find any words with a provided prexif, it return -1 value.
'''


class Solution:
    def __init__(self, sentence: str, searh_word: str) -> None:
        self.sentence = sentence
        self.searh_word = searh_word

    def is_prefix_of_word(self) -> int:
        i: int = 0
        sentence_words = self.sentence.split()
        for word in sentence_words:
            if word.startswith(self.searh_word):
                break
            else:
                i += 1

        return -1 if i >= len(sentence_words) else i + 1


case1: Solution = Solution(
    sentence="i love eating burger", searh_word="burg")
print(case1.is_prefix_of_word())    # Should ouptut 4

case2: Solution = Solution(
    sentence="i am tired", searh_word="you")
print(case2.is_prefix_of_word())    # Should ouptut -1
