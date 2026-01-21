#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        return 0
    for index in my_list:
        print("{:d}".format(index))
