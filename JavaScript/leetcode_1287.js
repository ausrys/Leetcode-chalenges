/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function (arr) {
    let c = 0;
    let curr = arr[0];
    for (let index = 0; index < arr.length; index++) {
        if (arr[index] === curr) {
            c++;
            if (arr.length / 4 < c) return arr[index];
        } else {
            c = 1;
            curr = arr[index];
        }
    }
};
