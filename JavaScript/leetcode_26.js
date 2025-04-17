/* 
Given an integer array nums sorted in non-decreasing order, remove the\
duplicates in-place such that each unique element appears only once.\
The relative order of the elements should be kept the same. Then\
return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,\
you need to do the following things:

Change the array nums such that the first k elements of nums contain the \
unique elements in the order they were present in nums initially.\
The remaining elements of nums are not important as well as the size of nums.
Return k.


In this problem we edit the list directly. First we create two variables,\
k to track the position of a number and number variable to track the
numbers and compare them.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
function removeDuplicates(nums) {
    let k = 1;
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] !== nums[k -1]) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k
}

console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))