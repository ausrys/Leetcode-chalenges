var binaryTreePaths = function(root) {
    let result = []
    function dfs(node, path) {
        if (!node) return
        path += String(node.val);
        if (!node.left  && !node.right) result.push(path)
        else {
            path += "->";
            dfs(node.left, path)
            dfs(node.right, path)
        };
    };
    dfs(root, "")
    return result
};