#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copied_list = my_list[:]
    if 0 <= idx < len(my_copied_list):
        my_copied_list[idx] = element
    return my_copied_list
