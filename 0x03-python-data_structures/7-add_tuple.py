#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_number1, a_number2, b_number1, b_number2 = 0, 0, 0, 0
    if len(tuple_a) >= 2:
        a_number1 = tuple_a[0]
        a_number2 = tuple_a[1]
    elif len(tuple_a) == 1:
        a_number1 = tuple_a[0]
    if len(tuple_b) >= 2:
        b_number1 = tuple_b[0]
        b_number2 = tuple_b[1]
    elif len(tuple_b) == 1:
        b_number1 = tuple_b[0]
    return a_number1 + b_number1, a_number2 + b_number2
