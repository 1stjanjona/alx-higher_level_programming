#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Define a rectangle."""

    number_of_instances = 0
    """the number of instances"""

    print_symbol = '#'
    """printed symbol"""

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle
        Args:
            width: width of rectangle
            height: hwight of rectangl
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        s = ""
        if self.width != 0 or self.height != 0:
            for x in range(self.__height):
                s += str(self.print_symbol) * self.__width + "\n"
        return s[:-1]

    def __repr__(self):
        """Return string representation of rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Print when instance deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest rectangle
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: if they are not instances
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
