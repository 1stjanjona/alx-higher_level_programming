#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Define a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print when instance deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """to get width"""
        return self.__width

    @width.setter(self, value):
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

    def __str__(self):
        """Print rectangle with #"""
        s = ""
        if self.__width != 0 and self.__height != 0:
            for x in range(self.__height):
                s += "\n".join("#" * self.__width)
        return s

    def __repr__(self):
        """Return string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
