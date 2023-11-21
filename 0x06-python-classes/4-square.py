#!/usr/bin/python3
"""Class Square."""


class Square:
    """Define Square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: size of square.
        """
        self.__size = size

    @property
    def size(self):
        """Property of square's size.

        Raises:
            TypeError: if size isn;t integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of Square.

        Returns:
            Size of current square area
        """
        return self.__size ** 2
