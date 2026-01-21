#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_number = 0
    roman_convert = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    for letter, next_letter in zip(roman_string, roman_string[1:]):
        value = roman_convert[letter]
        next_value = roman_convert[next_letter]
        roman_number += -value if value < next_value else value
    roman_number += roman_convert[roman_string[-1]]
    return roman_number
