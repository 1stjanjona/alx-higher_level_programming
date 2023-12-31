#!/usr/bin/python3
"""Class Square."""


class Square:
    """Define Square."""

    def __init__(self, size=0):
        """Constractor.

        Args:
            size: size of square.

        Raises:
            TypeError: If size isn't an integer
            ValueError: Is size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
