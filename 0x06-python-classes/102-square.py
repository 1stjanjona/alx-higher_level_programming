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
        """Property for square size.

        Raises:
            TypeError: If size isn't integer.
            ValueError: If size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of the current square.

        Returns:
            square size.
        """
        return self.__size ** 2

    def __eq__(self, comparator):
        """Eq equals to."""
        return self.area() == comparator.area()

    def __ne__(self, comparator):
        """Ne not equals to."""
        return self.area() != comparator.area()

    def __gt__(self, comparator):
        """gt greater than."""
        return self.area() > comparator.area()

    def __ge__(self, comparator):
        """ge greater or equals to."""
        return self.area() >= comparator.area()

    def __lt__(self, comparator):
        """lt lesser than."""
        return self.area() < comparator.area()

    def __le__(self, comparator):
        """le lesser than or equals to."""
        return self.area() <= comparator.area()
