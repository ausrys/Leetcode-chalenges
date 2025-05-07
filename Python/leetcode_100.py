'''
Given the roots of two binary trees p and q, write a function
to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) \
            -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return (
            self.is_same_tree(p.left, q.left) and
            self.is_same_tree(p.right, q.right)
        )
