#!/usr/bin/python3
"""
    2-matrix_divided.py
    Module that defines a method for dividing a matrix by float or integer
"""


def matrix_divided(matrix, div):
    """
    Function that takes a matrix as first parameter and a float or integer
    as second parameter and returns a new matrix of the divided elements
    of the original matrix

    Args:
        matrix (list): original matrix
        div (int, float): divisor

    Note:
        If matrix is not a list of lists of integers or floats,
        a TypeError exception is raised
        If each row of the matrix are not of the same size,
        a TypeError exception is raised
        If div is not an integer or a float, a TypeError exception is raised
        If div is equal to 0, a ZeroDivisionError exception is raised
        Otherwise, divide each element of the matrix by div and return a
        new matrix with elements rounded to 2 decimal places
    """
    for lst in matrix:
        if not isinstance(lst, list) or not isinstance(matrix, list) \
                or not all(isinstance(i, (int, float)) for i in lst):
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")

    if not all(len(lst) == len(matrix[0]) for lst in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float("inf") or div == -float("inf"):
        divided_matrix = [[0.0 for i in lst] for lst in matrix]
    else:
        divided_matrix = [[round(i / div, 2) for i in lst] for lst in matrix]

    return divided_matrix
