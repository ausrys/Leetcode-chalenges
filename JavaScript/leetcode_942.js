/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function (s) {
    let i = 0;
    let d = s.length;
    let result = [];
    for (let index = 0; index < s.length; index++) {
        if (s[index] === "I") {
            result.push(i);
            i++;
        } else {
            result.push(d);
            d--;
        }
    }
    if (s.at(-1) === "I") result.push(i);
    else result.push(d);
    return result;
};
