var generate = function(numRows) {
    let result = [];
    
    for (let i = 0; i < numRows; i++) {
        let row = Array(i + 1).fill(1); // Create row with i+1 elements, all 1

        for (let j = 1; j < i; j++) {
            row[j] = result[i - 1][j - 1] + result[i - 1][j]; // Fill middle values
        }

        result.push(row); // Push once per row
    }

    return result;
}