#!/usr/bin/python3
'''12-pascal_triangle.py Module'''


def pascal_triangle(n):
    """Return list of lists of integers representing pascal_triangle of n"""
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) is not n:
        p = pascal[-1]
        t = [1]
        for x in range(len(p) - 1):
            t.append(p[x] + p[x + 1])
        t.append(1)
        pascal.append(t)
    return pascal
