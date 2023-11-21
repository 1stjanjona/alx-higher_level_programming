#!/usr/bin/python3
"""Class Square."""


class Square:
    """Define Square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Size of Square

        Raises:
            TypeError: if size isn't an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of Square.

        Returns:
            The current square area.
        """
        return self.__size ** 2
