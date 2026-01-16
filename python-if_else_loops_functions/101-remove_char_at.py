#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for letter in range(len(str)):
        if (letter != n):
            str_cpy += str[letter]
    return str_cpy
