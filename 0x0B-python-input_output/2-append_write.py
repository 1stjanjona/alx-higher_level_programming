#!/usr/bin/python3
'''2-append_write.py Module.'''


def append_write(filename="", text=""):
    '''Return number of appended string at the end of text file'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
