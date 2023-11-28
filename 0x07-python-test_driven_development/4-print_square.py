#!/usr/bin/python3
"""Module print_square."""


def print_square(size):
    """Print a square with #.
    Args:
        size: length of square.
    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0
        TypeError: if size is float or < 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print((('#' * size + '\n') * size), end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
