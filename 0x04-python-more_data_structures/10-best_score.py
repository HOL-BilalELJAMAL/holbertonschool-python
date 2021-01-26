#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) != dict:
        return None
    sorted_items = sorted(a_dictionary.items(), reverse=True)
    return sorted_items[0][0]
