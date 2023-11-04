#!/usr/bin/python3
def no_c(my_string):
    removed = ""
    for ndx in range(0, len(my_string)):
        if my_string[ndx] != 'c' and my_string[ndx] != 'C':
            removed += my_string[ndx]
    return removed
