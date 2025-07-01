/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function (nums) {
    let j = 0;
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] % 2 === 0) {
            [nums[index], nums[j]] = [nums[j], nums[index]];
            j++;
        }
    }
    return nums;
};
