""" 
Given the root of a binary tree, check whether it is 
a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    is_mirror(t1.left, t2.right) and
                    is_mirror(t1.right, t2.left))
        return is_mirror(root, root)
