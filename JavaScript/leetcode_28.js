/*
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.
We check if provided needle exists in haystack and then check its index.
*/
function needle_in_stack(stack, needle) {
    if (stack.includes(needle)) return stack.indexOf(needle)
    return -1
}

console.log(needle_in_stack("asdasdaleetcode", "zleet"))  // -1
console.log(needle_in_stack("asasdasdaleetcoded", "leet")) // 9