/* 
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
*/

/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    let result = [];
    
    for (let i = 0; i <= rowIndex; i++) {
        let row = Array(i + 1).fill(1); // Create row with i+1 elements, all 1

        for (let j = 1; j < i; j++) {
            row[j] = result[i - 1][j - 1] + result[i - 1][j]; // Fill middle values
        }

        result.push(row); // Push once per row
    }

    return result.pop();
};