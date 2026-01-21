#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    new_list = []
    for element in my_list:
        new_list.append(replace if element == search else element)
    return new_list
