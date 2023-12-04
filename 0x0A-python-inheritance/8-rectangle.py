#!/usr/bin/python3
'''8-rectangle.py Module.'''
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
