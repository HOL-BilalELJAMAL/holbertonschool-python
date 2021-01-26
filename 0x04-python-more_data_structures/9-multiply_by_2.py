#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = dict(a_dictionary)
    b_dictionary.update((x, y * 2) for x, y in b_dictionary.items())
    return b_dictionary
