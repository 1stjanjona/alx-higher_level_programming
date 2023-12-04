#!/usr/bin/python3
'''10-square.py Module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square Class for Rectangle'''
    def __init__(self, size):
        '''Instantiation with size.
        Args:
        - size: must be private positive integer.
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area of square implementation'''
        return self.__size * self.__size
