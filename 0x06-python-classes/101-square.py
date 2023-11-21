#!/usr/bin/python3
"""Class Square."""


class Square:
    """Coordinate a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Define square.

        Args:
            size: size of square
            position: position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve, set the square size."""
        return self.__size

    @size.setter
    def size(self, value):
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
        not_tuple = not isinstance(value, tuple)
        len_not_2 = (len(value) != 2)
        all_not_int = not all(isinstance(n, int) for n in value)
        all_not_positive = not all(n > 0 for n in value)

        if not_tuple or len_not_2 or all_not_int or all_not_positive:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return area of current square."""
        return self.__size * self.__size

    def my_print(self):
        """Print square."""

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

    def __str__(self):
        """Define behaviour of my_print()."""
        if self.__size != 0:
            for x in range(self.__position[1]):
                print("")
        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")

            for z in range(self.__size):
                print("#", end="")
            if x != (self.__size - 1):
                print("")
        return ("")
