#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sum_numbers = 0
    value = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for ndx in reversed(roman_string):
        numbers = roman[ndx]
        if numbers >= value:
            sum_numbers += numbers
        else:
            sum_numbers -= numbers
        value = numbers
    return sum_numbers
