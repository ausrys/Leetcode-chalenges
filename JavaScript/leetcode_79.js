var exist = function (board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function backtrack(r, c, i) {
        // If all characters are matched
        if (i === word.length) return true;

        // Check boundaries and current character
        if (
            r < 0 ||
            c < 0 ||
            r >= rows ||
            c >= cols ||
            board[r][c] !== word[i]
        ) {
            return false;
        }

        // Temporarily mark the cell as visited
        const temp = board[r][c];
        board[r][c] = "#";

        // Explore all 4 directions
        const found =
            backtrack(r + 1, c, i + 1) ||
            backtrack(r - 1, c, i + 1) ||
            backtrack(r, c + 1, i + 1) ||
            backtrack(r, c - 1, i + 1);

        // Restore the cell
        board[r][c] = temp;

        return found;
    }

    // Try to start from each cell
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (backtrack(r, c, 0)) return true;
        }
    }

    return false;
};
