'''
Given the root of a binary tree, return the postorder
traversal of its nodes' values.
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []

        def traversing(node):
            if not node:
                return
            if node.left:
                traversing(node.left)
            if node.right:
                traversing(node.right)
            node_list.append(node.val)

        traversing(root)
        return node_list
