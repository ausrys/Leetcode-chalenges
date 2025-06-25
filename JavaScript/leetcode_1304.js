/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    if (n % 2 === 0) {
        let result = [];
        for (let index = -n +1; index < n +1; index+= 2) {
            result.push(index)
        };
        return result
    }
    else {
        let result = [];
        for (let index = -n +1; index < n; index+= 2) {
            result.push(index)
        };
        return result
    }
};