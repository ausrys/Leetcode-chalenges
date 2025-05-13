'''
Write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string "".

I solved this problem by getting the shortest string in the array and then
looping trough the array checking if the elements starts with shortest
string characters
'''

from typing import List


def longest_common_prefix(strs: List[str]):
    shortest_string = min(strs, key=len)
    i = 1
    while i <= len(shortest_string):
        for string in strs:
            if string.startswith(shortest_string[0:i]) is False:
                return shortest_string[0:i-1]
        i += 1
    return shortest_string[0:i-1]


print(longest_common_prefix(["dog", "racecar", "car"]))
