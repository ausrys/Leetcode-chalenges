'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return\
the subtree rooted with that node. If such a node does not exist, return null.
'''
# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search_bst(self, root: Optional[TreeNode], val: int)\
            -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.search_bst(root.left, val)
        else:
            return self.search_bst(root.right, val)
