/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
    const stones_counter = {};
    let result = 0;
    [...stones].forEach((element) => {
        stones_counter[element] = (stones_counter[element] || 0) + 1;
    });
    for (let index = 0; index < jewels.length; index++) {
        if (stones_counter[jewels[index]])
            result += stones_counter[jewels[index]];
    }
    return result;
};
