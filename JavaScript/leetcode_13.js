/* 
Given a roman numeral, convert it to an integer.
*/

var romanToInt = function(s) {
    let totalSum = 0;
    const romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000};
    for (let i = 0; i < s.length; i++) {
        if (i < s.length -1 && romans[s[i]] < romans[s[i+1]]) totalSum -= romans[s[i]]
        else totalSum += romans[s[i]]
    };
    return totalSum
};

console.log(romanToInt("III"));