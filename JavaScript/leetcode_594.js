/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function (nums) {
    let maxl = 0;
    const freqMap = new Map();
    for (const item of nums) {
        freqMap.set(item, (freqMap.get(item) || 0) + 1);
    }
    for (const key of freqMap.keys()) {
        if (freqMap.has(key + 1)) {
            maxl = Math.max(maxl, freqMap.get(key) + freqMap.get(key + 1));
        }
    }
    return maxl;
};
findLHS([1, 2, 2]);
