/* 
Given a binary array nums, return the maximum number of consecutive 1's in the array.
*/

var findMaxConsecutiveOnes = function(nums) {
    let maxN = 0;
    let temp = 0;
    for (let num of nums) {
        if (num ==1 ) {
            temp++;
            maxN = Math.max(maxN, temp);
        }
        else temp = 0
        
    };
    return maxN
};