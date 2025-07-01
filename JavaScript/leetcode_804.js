/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function (words) {
    let seen = new Set();
    const morse = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ];

    for (let index = 0; index < words.length; index++) {
        let morse_string = "";
        let word_letters = [...words[index]];
        for (let index = 0; index < word_letters.length; index++) {
            morse_string = morse_string.concat(
                morse[word_letters[index].charCodeAt() - 97],
            );
        }
        seen.add(morse_string);
    }
    return seen.size;
};
