#!/usr/bin/python3
'''0-read_file.py Module.'''


def read_file(filename=""):
    '''Read a text file and print it.'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
