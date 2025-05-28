from typing import List


def length_of_longest_substring(s: str) -> int:
    string_stack: List[str] = []
    max_len = 0

    for i in s:
        if i in string_stack:
            # Remove characters from the front until the duplicate is removed
            while i in string_stack:
                string_stack.pop(0)
        string_stack.append(i)
        max_len = max(max_len, len(string_stack))

    return max_len


print(length_of_longest_substring("aab"))
