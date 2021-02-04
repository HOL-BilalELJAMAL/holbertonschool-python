#!/usr/bin/python3
"""
    100-matrix_mul.py
    Module that defines a method for multiplying 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function that takes 2 matrices as parameter and returns
    a new matrix whose elements are the multiplication of each
    element of each matrix

    Args:
        m_a (list): First matrix
        m_b (list): Second matrix

    Note:
        If m_a is not a list, a TypeError exception is raised
        If m_b is not a list, a TypeError exception is raised
        If m_a is not a list of a list, a TypeError exception is raised
        If m_b is not a list of a list, a TypeError exception is raised
        If m_a is an empty list or empty list of list, a ValueError
        exception is raised
        If m_b is an empty list or empty list of list, a ValueError
        exception is raised
        If m_a does not contain only integers or floats, a TypeError
        exception is raised
        If m_b does not contain only integers or floats, a TypeError
        exception is raised
        If m_a does not contain lists of same size, a TypeError
        exception is raised
        If m_b does not contain lists of same size, a TypeError
        exception is raised
        If m_a or m_b is not rectangle, a ValueError
        exception is raised
        Otherwise, return a new matrix whose elements are the multiplication
        of each element of each matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(lst, list) for lst in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(lst, list) for lst in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a in [[], [[]]]:
        raise ValueError("m_a can't be empty")
    if m_b in [[], [[]]]:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(i, (int, float)) for i in lst) for lst in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(i, (int, float)) for i in lst) for lst in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = [[0 for i in m_b[0]] for j in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
