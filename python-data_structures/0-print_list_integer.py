#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        return
    for index in my_list:
        print("{}".format(index))
