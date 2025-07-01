/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function (nums) {
    let result = [];
    for (let index = 0; index < array.length - 1; index += 2) {
        result.push(...Array(nums[index]).fill(nums[i + 1]));
    }
    return result;
};
