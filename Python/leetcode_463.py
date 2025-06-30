from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:      # up
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:      # left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # right
                    perimeter -= 1

    return perimeter


print(island_perimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
