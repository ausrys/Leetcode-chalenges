function commonChars(words) {
    // Helper to count characters in a word
    const countChars = (word) => {
        const count = Array(26).fill(0);
        for (let char of word) {
            count[char.charCodeAt(0) - 97]++;
        }
        return count;
    };

    // Initialize with the count from the first word
    let common = countChars(words[0]);

    // Intersect counts with each next word
    for (let i = 1; i < words.length; i++) {
        const currentCount = countChars(words[i]);
        for (let j = 0; j < 26; j++) {
            common[j] = Math.min(common[j], currentCount[j]);
        }
    }

    // Build result array from final counts
    const result = [];
    for (let i = 0; i < 26; i++) {
        while (common[i] > 0) {
            result.push(String.fromCharCode(i + 97));
            common[i]--;
        }
    }

    return result;
}
