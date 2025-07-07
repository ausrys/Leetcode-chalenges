/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function (arr) {
    let c = {};
    arr.forEach((ele) => {
        c[ele] = (c[ele] || 0) + 1;
    });
    return new Set(Object.values(c)).size == Object.values(c).length;
};
