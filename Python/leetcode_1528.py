from typing import List


def restore_string(s: str, indices: List[int]) -> str:
    f_list = [0] * len(s)
    for c, i in enumerate(s):
        f_list[indices[c]] = i
    return ''.join(f_list)


print(restore_string("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
