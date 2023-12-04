#!/usr/bin/python3
'''7-base_geometry.py Module.'''


class BaseGeometry:
    '''Class for public instance'''

    def area(self):
        '''Raise exception if area not implemented.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validate value
        Args:
        - value: raise TypeError and ValueError if not int and <= 0
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
