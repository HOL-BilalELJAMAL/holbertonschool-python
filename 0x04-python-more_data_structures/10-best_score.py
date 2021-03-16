#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) != dict or not a_dictionary:
        return None
    list_keys = list(a_dictionary.keys())
    list_values = list(a_dictionary.values())
    sorted_values = sorted(list_values, reverse=True)
    max_value = sorted_values[0]
    return list_keys[list_values.index(max_value)]
