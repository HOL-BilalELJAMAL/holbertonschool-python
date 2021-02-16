#!/usr/bin/python3
"""module"""


def pascal_triangle(n):
    """pascal's triangle"""

    if n <= 0:
        return []
    a = []
    for i in range(n):
        a.append([])
        a[i].append(1)
        if i != 0:
            for j in range(1, i):
                a[i].append(a[i - 1][j - 1]+a[i - 1][j])
            if n != 0:
                a[i].append(1)
    return a
