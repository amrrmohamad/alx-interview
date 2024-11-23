#!/usr/bin/python3
"""
Rotate 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """rotate two matrix 90 degrees.
    Args:
        matrix : a matrix contain a lists
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # tmp variable
            tmp = matrix[i][j]
            # change top to left
            matrix[i][j] = matrix[x][i]
            # change left to bottom
            matrix[x][i] = matrix[y][x]
            # change bottom tp right
            matrix[y][x] = matrix[j][y]
            # change right to top
            matrix[j][y] = tmp
