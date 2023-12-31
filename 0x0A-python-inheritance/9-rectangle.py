#!/usr/bin/python3
'''9-rectangle.py Module.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class of BaseGeometry'''

    def __init__(self, width, height):
        '''Instantiation of Rectangle.
        Args:
            width & height: must be private positive integers.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Implemented area() method'''
        return self.__width * self.__height

    def __str__(self):
        '''Return str of rectangle'''
        return f"[Rectangle] {self.__width}/{self.__height}"
