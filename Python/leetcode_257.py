'''
Given the root of a binary tree, return all root-to-leaf
paths in any order.

A leaf is a node with no children.
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    result: List[str] = []

    def dfs(node, path):
        if not node:
            return
        # Add current node to path
        path += str(node.val)
        # If it's a leaf, add the path to result
        if not node.left and not node.right:
            result.append(path)
        else:
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

    dfs(root, "")
    return result
