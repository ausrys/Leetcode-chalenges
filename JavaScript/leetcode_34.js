/* 
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
*/

var searchRange = function(nums, target) {
    function findLeft() {
        let left = 0;
        let right = nums.length -1;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (nums[mid] < target ) left = mid +1
            else right = mid -1
        };
        return left
    };
    function findRight() {
        let left = 0;
        let right = nums.length -1;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (nums[mid] <= target ) left = mid +1
            else right = mid -1
        };
        return right
    };
    let left_index = findLeft();
    let right_index = findRight();
    if(left_index <= right_index) return [left_index, right_index]
    return [-1, -1]
};