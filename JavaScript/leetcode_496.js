/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
    let next_greater = new Map();
    let stack = [];
    for (let index = 0; index < nums2.length; index++) {
        while (stack.length !== 0 && nums2[index] > stack.at(-1)) {
            let prev = stack.pop();
            next_greater.set(prev, nums2[index]);
        }
        stack.push(nums2[index]);
    }
    for (let index = 0; index < stack.length; index++) {
        next_greater.set(stack[index], -1);
    }
    return nums1.map((num) => next_greater.get(num));
};

console.log(nextGreaterElement((nums1 = [4, 1, 2]), (nums2 = [1, 3, 4, 2])));
