var isValid = function (s) {
    let stack = [];
    const bracket_map = { ")": "(", "}": "{", "]": "[" };

    for (let char of s) {
        if (Object.values(bracket_map).includes(char)) {
            stack.push(char);
        } else if (char in bracket_map) {
            if (
                stack.length === 0 ||
                stack[stack.length - 1] !== bracket_map[char]
            ) {
                return false;
            }
            stack.pop();
        }
    }

    return stack.length === 0;
};

console.log(isValid("()"));
