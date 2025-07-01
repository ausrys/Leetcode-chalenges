/* 
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

*/

var countNodes = function (root) {
    function getHeight(node) {
        let h = 0;
        while (node) {
            h++;
            node = node.left;
        }
        return h;
    }
    if (!root) return 0;
    left_height = getHeight(root.left);
    right_height = getHeight(root.right);
    if (left_height === right_height)
        return (1 << left_height) + countNodes(root.right);
    return (1 << right_height) + countNodes(root.left);
};
