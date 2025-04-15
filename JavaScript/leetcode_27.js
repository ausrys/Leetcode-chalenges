/*
Given an integer array nums and an integer val, remove all occurrences of val\
in nums in-place. The order of the elements may be changed. Then return the\
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, \
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the \
elements which are not equal to val. The remaining elements of nums are not\
important as well as the size of nums.
Return k.

This problem has to solved with in-place method, meaning the list must be\
modified directly. We simply check if number in the list is not\
equal to the val and simply change original nums list values
*/

function remove_element(array, element) {
    let k = 0;
    for (num of array) {
        if (num !== element) k++;
    }
    return k;
}

console.log(remove_element([3, 2, 2, 3], 3))
console.log(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))