#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 and my_list_2:
        new_list = [0] * list_length
        for i in range(0, list_length):
            res = 0
            try:
                res = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except ValueError:
                print("wrong type")
            except IndexError:
                print("out of range")
            except:
                pass
            finally:
                if res != 0:
                    new_list[i] = res
        return new_list
