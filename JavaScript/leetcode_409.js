var longestPalindrome = function(s) {
    let counts = new Map();
    for (let char of s) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }

    let length = 0;
    let oddFound = false;

    for (let count of counts.values()) {
        if (count % 2 === 0) {
            length += count;
        } else {
            length += count - 1;
            oddFound = true;
        }
    }

    if (oddFound) length += 1;

    return length;
};
