#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum, mult = 0, 0
    for i in range(len(my_list)):
        mult += my_list[i][0] * my_list[i][1]
        sum += my_list[i][1]
    return mult/sum
