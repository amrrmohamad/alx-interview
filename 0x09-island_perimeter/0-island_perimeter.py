#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculat perimeter for island described in grid
    Return:
        perimeter for island
    """

    var = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    var += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    var += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    var += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    var += 1
    return var
