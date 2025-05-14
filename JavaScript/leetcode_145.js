/* 
Given the root of a binary tree, return the postorder traversal of its nodes' values.
*/

var preorderTraversal = function(root) {
    let nodes = [];
    function traverse(node) {
        if (!node) return
        
        if (node.left) traverse(node.left)
        if (node.right) traverse(node.right)
        nodes.push(node.val)
    }
    traverse(root);
    return nodes;
};