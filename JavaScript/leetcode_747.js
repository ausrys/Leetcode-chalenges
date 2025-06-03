/* 
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array.
 If it is, return the index of the largest element, or return -1 otherwise.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    let sorted = nums.toSorted((a, b) => a - b)
    console.log(sorted.slice(-1)[0]);
    if (sorted.slice(-1)[0] < sorted.slice(-2, -1)[0] * 2) return -1
    return nums.indexOf(sorted.slice(-1)[0])
}

dominantIndex([3,6,1,0]);