/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function (operations) {
    const opers = new Set(["C", "D", "+"]);
    let points = [];
    for (let index = 0; index < operations.length; index++) {
        if (!opers.has(operations[index]))
            points.push(Number(operations[index]));
        else if (operations[index] === "C") points.pop();
        else if (operations[index] === "D") points.push(2 * points.at(-1));
        else points.push(points.at(-1) + points.at(-2));
    }
    let sum = 0;
    for (let index = 0; index < points.length; index++) {
        sum += points[index];
    }
    return sum;
};

console.log(calPoints(["5", "2", "C", "D", "+"]));
