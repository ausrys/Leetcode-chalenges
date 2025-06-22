/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let arr = new Array(s.length).fill(0);
    for (let index = 0; index < s.length; index++) {
        arr[indices[index]] = s[index];
    };
    return arr.join("")
};