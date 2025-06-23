/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    const sh = heights.toSorted((a,b) => a-b);
    let result = 0;
    for (let index = 0; index < sh.length; index++) {
        if (sh[index] !== heights[index]) result++;
    };
    return result
};