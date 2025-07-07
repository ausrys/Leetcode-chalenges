var intToRoman = function (num) {
    const valMap = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ];

    let roman = "";
    for (let [value, symbol] of valMap) {
        const count = Math.floor(num / value);
        num %= value;
        roman += symbol.repeat(count);
    }

    return roman;
};

console.log(intToRoman(345));
