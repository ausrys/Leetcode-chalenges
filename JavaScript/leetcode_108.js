/* 
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
*/
var sortedArrayToBST = function(nums) {
    function buildBST(left, right) {
        if (left > right) return null;
        
        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(nums[mid]);
        node.left = buildBST(left, mid - 1);
        node.right = buildBST(mid + 1, right);
        return node;
    }

    return buildBST(0, nums.length - 1);
};