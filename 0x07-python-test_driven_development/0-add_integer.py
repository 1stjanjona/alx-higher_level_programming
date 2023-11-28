#!/usr/bin/python3
"""Module of add_integer function."""


def add_integer(a, b=98):
    """Addition of a and b.

    Args:
        a: first int or float
        b: constant b=98, second int or float

    Raises:
        TypeError: if a and b are not integers or floats.

    Returns:
        addition of a and b casted to integers.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
