'''
Given the root of a binary search tree (BST) with duplicates,
return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal
to the node's key.
The right subtree of a node contains only nodes with keys greater than
or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

'''
# Definition for a binary tree node.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_mode(self, root: Optional[TreeNode]) -> List[int]:
        nodes_map = {}
        if not root:
            return [0]

        def get_modes(root):
            if not root:
                return
            if root.val not in nodes_map:
                nodes_map[root.val] = 1
            if root.val in nodes_map:
                nodes_map[root.val] += 1
            return (get_modes(root.left), get_modes(root.right))
        get_modes(root)
        max_value = max(nodes_map.values())
        res = [key for key in nodes_map if nodes_map[key] == max_value]
        return res
