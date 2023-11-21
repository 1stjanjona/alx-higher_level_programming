#!/usr/bin/python3
"""Class Square."""


class Square:
    """Define square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: size of square.
        """
        self.__size = size

    @property
    def size(self):
        """Property for the size of current square

        Raises:
            TypeError: if size isn't integer
            ValueError: is size < 0
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
        """Area of the current square.

        Returns:
            size of square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print in stdout the square."""
        for x in range(self.size):
            for y in range(self.size):
                if y is self.size - 1 and x != y:
                    print("#", end="\n")
                else:
                    print("#", end="")
        print()
