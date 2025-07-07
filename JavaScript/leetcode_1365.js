/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
    const original = [...nums];
    nums.sort((a, b) => a - b);
    let m = new Map();
    for (let index = 0; index < nums.length; index++) {
        if (!m.has(nums[index])) m.set(nums[index], index);
    }
    return original.map((n) => m.get(n));
};

console.log(smallerNumbersThanCurrent([8, 1, 2, 2, 3]));
