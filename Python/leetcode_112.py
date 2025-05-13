'''
Given the root of a binary tree and an integer targetSum, return true
if the tree has a root-to-leaf path such that adding up all the values
along the path equals targetSum.

A leaf is a node with no children.
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    def traverse_pre_order(node, target):
        if not node:
            return False
        if not node.left and not node.right and node.val == target:
            return True
        return traverse_pre_order(node.left, target - node.val) or \
            traverse_pre_order(node.right, target - node.val)
    return traverse_pre_order(root, target_sum)
