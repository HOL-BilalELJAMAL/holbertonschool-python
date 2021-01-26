#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_list = list(map(lambda x: x**2, matrix[i]))
        new_matrix.append(new_list)
    return new_matrix
