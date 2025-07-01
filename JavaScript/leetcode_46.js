/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    let result = [];
    /**
     * @param {number[]} path
     * @param {Set} used
     */
    function backtrack(path, used) {
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }
        for (let index = 0; index < nums.length; index++) {
            if (used.has(nums[index])) continue;
            path.push(nums[index]);
            used.add(nums[index]);
            backtrack(path, used);
            path.pop();
            used.delete(nums[index]);
        }
    }
    backtrack([], new Set());
    return result;
};
