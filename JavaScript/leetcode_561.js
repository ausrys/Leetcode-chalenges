/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
    nums.sort((a, b) => a - b);
    let sum = 0;
    for (let i = 0; i < nums.length; i += 2) {
        sum += Math.min(nums[i], nums[i + 1]);
    }
    return sum;
};

console.log(arrayPairSum([1, 4, 3, 2]));
