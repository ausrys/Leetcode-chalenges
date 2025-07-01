/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
    let reversed_l = s.split(" ");
    let reversed = reversed_l.map((word) => [...word].reverse().join(""));
    return reversed.join(" ");
};
