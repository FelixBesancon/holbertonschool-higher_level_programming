#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return {}
    new_dict = dict()
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
