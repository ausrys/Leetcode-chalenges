'''
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter
cell may not be used more than once.
'''


def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):  # All letters matched
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False
        if board[r][c] != word[i]:
            return False

        # Temporarily mark the cell as visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all 4 directions
        found = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)
        )

        # Restore the cell
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
