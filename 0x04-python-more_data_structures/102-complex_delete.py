#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    indexes = []
    if value in a_dictionary.values():
        for i in a_dictionary:
            if a_dictionary[i] == value:
                indexes += [i]
        for index in indexes:
            del a_dictionary[index]
    return a_dictionary
