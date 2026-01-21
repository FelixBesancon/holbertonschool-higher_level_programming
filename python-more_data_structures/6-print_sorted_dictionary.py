#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return 0
    sorted_dictionary = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dictionary.items():
        print("{}: {}".format(key, value))
