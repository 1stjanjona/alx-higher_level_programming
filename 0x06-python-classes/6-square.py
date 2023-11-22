#!/usr/bin/python3
"""Class Square."""


class Square:
    """Coordinate a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Define square.


        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve, set the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size.


        Args:
            value (int): size value.
        A
        Reises:
            TypeError: if size not integer
            ValueError: if size < 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """retrive, set the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """SEt position for current square.

        Args:
            value (tuple): position of square.
        Raises:
            TypeError: if position is not tuple of integers.
        """
        if not isinstance(value, tuple):
            raise TypeError('position maust be a tuple')
        if len(value) != 2:
            raise ValueError('position must be a tuple of 2 integers')
        if not all(isinstance(n, int) for n in value):
            raise TypeError('position must be a tuple of 2 integers')
        if not all(n > 0 for n in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return area of current square."""
        return self.__size ** 2

    def my_print(self):
        """Print square with #.

        If size == 0, return empty line.
        if position[1] > 0, spaces will be added.

        Returns:
            print square.
        """
        if self.__size == 0:
            print()
            return

        for x in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print()
