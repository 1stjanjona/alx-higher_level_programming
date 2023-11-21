#!/usr/bin/python3
"""Define the Python class MagicClass."""
import math
class MagicClass:
    """Python bytecode."""

    def __init__(self, radius=0):
        """Init MsgicClass.
        Args:
            radius: float or int radius of MagicClass
        """
        self.radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    
    def area(self):
        """Return area."""
        return self.__radius ** 2 * math.pi
    
    def circumference:
        """Return circumference."""
        return 2 * math.pi * self.__radius
