/* 
Given the root of a binary tree, return the preorder traversal of its nodes' values.
*/

var preorderTraversal = function(root) {
    let nodes = [];
    function traverse(node) {
        if (!node) return
        nodes.push(node.val)
        if (node.left) traverse(node.left)
        if (node.right) traverse(node.right)
    }
    traverse(root);
    return nodes;
};