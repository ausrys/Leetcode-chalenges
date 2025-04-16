/*
 Reverse Degree of a String
 Given a string s, calculate its reverse degree.

 The reverse degree is calculated as follows:
    For each character, multiply its position in the reversed alphabet ('a' = \
    26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
    Sum these products for all characters in the string.
*/

function reverse_degree(string) {
    let result = 0;
    for (let i in string) {
        result += Math.abs((string.charCodeAt(i)- 123) * (parseInt(i)+1));
    };
    return result;
}

console.log(reverse_degree("zaza")) // 160