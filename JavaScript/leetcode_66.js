var plusOne = function (digits) {
    for (let index = digits.length - 1; index >= 0; index--) {
        if (digits[index] < 9) {
            digits[index]++;
            return digits;
        }
        digits[index] = 0;
    }
    return [1].concat(digits);
};

console.log(plusOne([9]));
