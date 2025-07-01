/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function (s1, s2) {
    let accurences = {};
    const s1_l = s1.split(" ");
    const s2_l = s2.split(" ");
    for (let index = 0; index < s1_l.length; index++) {
        accurences[s1_l[index]] = (accurences[s1_l[index]] || 0) + 1;
    }
    for (let index = 0; index < s2_l.length; index++) {
        accurences[s2_l[index]] = (accurences[s2_l[index]] || 0) + 1;
    }
    const result = Object.keys(accurences).filter(
        (word) => accurences[word] === 1,
    );
    return result;
};

console.log(uncommonFromSentences("this apple is sweet", "this apple is sour"));
