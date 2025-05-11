/* 
Given the root of a binary tree, return the inorder traversal of its nodes' values.
*/

var inorderTraversal = function (root) {
  let results = [];
  function inOrder(node) {
    if (!node) return;
    inOrder(node.left);
    results.push(node.val);
    inOrder(node.right);
  }
  inOrder(root);
  return results;
};
