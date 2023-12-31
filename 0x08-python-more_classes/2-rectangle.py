#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Define a rectangle."""
    def __init__(self, width=0, height=0):
        """Instantiation of rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
