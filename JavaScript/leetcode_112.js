/* 
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
*/
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */

var hasPathSum = function (root, targetSum) {
<<<<<<< HEAD
  if (!root) return false;
  if (!root.left && !root.right && root.val === targetSum) return true;
  return (
    hasPathSum(root.left, targetSum - root.val) ||
    hasPathSum(root.right, targetSum - root.val)
  );
=======
    if (!root) return false;
    if (!root.left && !root.right && root.val === targetSum) return true;
    return (
        hasPathSum(root.left, targetSum - root.val) ||
        hasPathSum(root.right, targetSum - root.val)
    );
>>>>>>> a240f511499660ef602885c94b58faa12d2f12e8
};
