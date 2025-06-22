/**
 * @param {string} sentence
 * @return {string}
 */
var toGoatLatin = function(sentence) {
    const vovels = new Set (['a', 'e', 'i', 'o', 'u']);
    let repeat = 1;
    let flist = [];
    let s = sentence.split(" ");
    for (let index = 0; index < s.length; index++) {
        if (vovels.has(s[index][0].toLowerCase())) {
            let w = s[index] + 'ma' + 'a'.repeat(repeat);
            flist.push(w)
            repeat++
        }
        else {
            let w = s[index].slice(1) + s[index][0] + 'ma' + 'a'.repeat(repeat)
            repeat++;
            flist.push(w)
        }
        
    }
    return flist.join(" ")
};