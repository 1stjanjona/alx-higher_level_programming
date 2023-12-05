#!/usr/bin/python3
'''100-append_after.py Module'''


def append_after(filename="", search_string="", new_string=""):
    """Insert line of text to file"""
    with open(filename, 'r', encoding="utf-8") as f:
        lines = []
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        with open(filename, 'w', encoding="utf-8") as f:
            f.writelines(lines)
