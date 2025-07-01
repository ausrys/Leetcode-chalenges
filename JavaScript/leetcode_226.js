/* 
Given the root of a binary tree, invert the tree, and return its root.
*/

var invertTree = function (root) {
    if (!root) return null;

    // Swap left and right
    [root.left, root.right] = [root.right, root.left];

    // Recursively invert subtrees
    invertTree(root.left);
    invertTree(root.right);

    return root;
};
