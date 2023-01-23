#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
        'XC': 90, 'CD': 400, 'CM': 900
    }
    number = 0
    x = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    while x < len(roman_string):
        if roman_string[x:x+2] in roman_dictionary:
            number += roman_dictionary[roman_string[x:x+2]]
            x = x + 2
        else:
            number += roman_dictionary[roman_string[x]]
            x = x + 1
    return number
