var findTheDifference = function (s, t) {
    let sdict = {};
    let tdict = {};
    for (const letter of s) {
        if (!(letter in sdict)) {
            sdict[letter] = 1;
        } else sdict[letter]++;
    }
    for (const letter of t) {
        if (!(letter in tdict)) {
            tdict[letter] = 1;
        } else tdict[letter]++;
    }
    for (const letter of t) {
        if (!(letter in tdict) || sdict[letter] !== tdict[letter])
            return letter;
    }
    return t[0];
};
