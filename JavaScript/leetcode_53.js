/* 
Given an integer array nums, find the subarray with the largest sum, and return its sum.
*/

var maxSubArray = function (nums) {
    let maxSum = -10000;
    let currentSum = 0;
    for (const num of nums) {
        currentSum += num;
        maxSum = Math.max(maxSum, currentSum);
        currentSum = Math.max(currentSum, 0);
    }
    return maxSum;
};
