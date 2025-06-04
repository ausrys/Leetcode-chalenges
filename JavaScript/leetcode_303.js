/* 
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right
 inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

*/

/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    let N = nums.length;
    this.sum_arr = new Array(N).fill(0)
    for (let index = 0; index < N; index++) {
        this.sum_arr[index +1] = this.sum_arr[index] + nums[index]
    }
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    return this.sum_arr[right+1] - this.sum_arr[left]
};

let obj = new NumArray([-2,0,3,-5,2,-1])
console.log(obj.sumRange(0, 2));