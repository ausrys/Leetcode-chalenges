/* 
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.
You must write an algorithm with O(log n) runtime complexity.
The main proble here is to make this algorithm logarithmic
we can achieve this by splitting the array in half, thus
shortening the problem everytime by 2

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

function searchInsert(nums, target) {
    let left = 0;
    let right = nums.length;
    while (left <= right) {
        mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return left;
}

console.log(searchInsert([2], 2));
