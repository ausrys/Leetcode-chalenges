/* 
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
*/
var thirdMax = function (nums) {
    if (nums.length == 1) return nums[0];
    let uni = [...new Set(nums)];
    function compareNumbers(a, b) {
        return a - b;
    }
    let sorted = uni.sort(compareNumbers);
    if (sorted.length >= 3) return sorted[sorted.length - 3];
    else return sorted[sorted.length - 1];
};

console.log(thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3]));
