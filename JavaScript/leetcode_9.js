/*
Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
In this problem I converted the number into the string and
reversed the string. Then I compared both strings to see if they are equal
*/

function polindrome(num) {
    return String(num) == String(num).split("").reverse().join("");
}

console.log(polindrome(121));
console.log(polindrome(1213));
console.log(polindrome(-121));
