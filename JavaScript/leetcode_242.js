/* 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
*/

var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;

    const count = Array(26).fill(0); // 26 letters in the alphabet

    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - 'a'.charCodeAt(0)] += 1;
        count[t.charCodeAt(i) - 'a'.charCodeAt(0)] -= 1;
    }

    return count.every(c => c === 0);
};