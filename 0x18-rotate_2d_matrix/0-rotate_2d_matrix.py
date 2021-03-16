#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
Module that defines a function that rotates a matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Function that rotates a matrix 90 degrees clockwise

    Args:
        matrix (list): Matrix
    """
    n = len(matrix)
    for i in range(n // 2):
        y = n - i - 1
        for j in range(i, y):
            x = n - 1 - j
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
