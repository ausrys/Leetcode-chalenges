/* 

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.*/

var findMode = function(root) {
    const nodesMap = {};

    if (!root) return [0];

    function getModes(node) {
        if (!node) return;

        if (!(node.val in nodesMap)) {
            nodesMap[node.val] = 1;
        } else {
            nodesMap[node.val]++;
        }

        getModes(node.left);
        getModes(node.right);
    }

    getModes(root);

    const maxCount = Math.max(...Object.values(nodesMap));
    return Object.keys(nodesMap)
        .filter(key => nodesMap[key] == maxCount)
        .map(Number);  // Convert string keys back to numbers
};