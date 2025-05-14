'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        # If one of the subtrees is missing, we shouldn't consider its depth
        # (as it's 0)
        if not root.left:
            return 1 + self.min_depth(root.right)
        if not root.right:
            return 1 + self.min_depth(root.left)

        # If both subtrees exist, take the minimum depth
        return 1 + min(self.min_depth(root.left), self.min_depth(root.right))
