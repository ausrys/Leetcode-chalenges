/* 

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

function twoSum(nums, target) {
    let num_map = {};
    for (let index = 0; index < nums.length; index++) {
        let complement = target - nums[index];
        if (Object.hasOwn(num_map, complement))
            return [num_map[complement], index];
        num_map[nums[index]] = index;
    }
    return [];
}

console.log(twoSum([3, 3], 6));
