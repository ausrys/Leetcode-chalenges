var invertTree = function(root) {
    if (!root) return null;
    
    // Swap left and right
    [root.left, root.right] = [root.right, root.left];
    
    // Recursively invert subtrees
    invertTree(root.left);
    invertTree(root.right);
    
    return root;
};