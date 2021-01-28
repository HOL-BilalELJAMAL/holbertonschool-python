#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    try:
        my_new_list = [0] * list_length
        if my_list_1 and my_list_2:
            for i in range(list_length):
                res = 0
                try:
                    res = my_list_1[i] / my_list_2[i]
                except ZeroDivisionError:
                    print("division by 0")
                except TypeError:
                    print("wrong type")
                except IndexError:
                    print("out of range")
                finally:
                    if res != 0:
                        my_new_list[i] = res
    except (TypeError, ValueError):
        pass
    return my_new_list
