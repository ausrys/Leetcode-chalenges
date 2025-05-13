'''
Given the root of a binary tree, return the preorder traversal
of its nodes' values.
'''


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []

        def traversing(node):
            if not node:
                return
            node_list.append(node.val)
            if node.left:
                traversing(node.left)
            if node.right:
                traversing(node.right)
        traversing(root)
        return node_list
