#!/usr/bin/python3
def remove_char_at(str, n):
    array = ""
    for index, char in enumerate(str):
        if index != n:
            array += char
    return array
