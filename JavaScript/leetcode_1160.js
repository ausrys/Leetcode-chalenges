var countCharacters = function (words, chars) {
    const charCount = new Array(26).fill(0);
    let result = 0;

    for (const ch of chars) {
        charCount[ch.charCodeAt() - 97]++;
        // charCount.set(ch, (charCount.get(ch) || 0) + 1)
    }

    for (const word of words) {
        if (canFormWord(word, charCount)) {
            result += word.length;
        }
    }

    return result;
};

function canFormWord(word, availableChars) {
    const charCount = new Array(26).fill(0);

    for (const char of word) {
        const pos = char.charCodeAt() - 97;
        if (++charCount[pos] > availableChars[pos]) {
            return false;
        }
    }

    return true;
}
