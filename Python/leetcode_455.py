'''
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie
that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child
i will be content. Your goal is to maximize the number of your content
children and output the maximum number.
'''

from typing import List


def find_content_children(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1  # This child is content
        cookie += 1  # Move to the next cookie

    return child
