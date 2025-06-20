/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    let new_s = s;
    for (let index = 0; index < s.length; index++) {
        new_s = new_s.slice(1).concat(s[index]);
        if (new_s === goal) return true
    };
    return false
};