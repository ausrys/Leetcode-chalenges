'''
Given the root of a binary tree, invert the tree, and return its root.
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
