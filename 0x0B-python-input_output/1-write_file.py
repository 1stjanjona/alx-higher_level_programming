#!/usr/bin/python3
'''1-write_file.py Module.'''


def write_file(filename="", text=""):
    '''Write string to text file and return the number of its characters.'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
