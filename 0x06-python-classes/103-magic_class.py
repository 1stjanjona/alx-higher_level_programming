#!/usr/bin/python3
"""Define the Python class MagicClass."""


import math


class MagicClass:
    """Python bytecode.

    Attributes:
        __radius (float or int): radius of Magical circle.
    """

    def __init__(self, radius=0):
        """Init MsgicClass.

        Args:
            radius: float or int radius of MagicClass.
        Raises:
            TypeError: if radius is not a number
        """
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius
    
    def area(self):
        """Calculate and Return area.

        Returns:
            float: area of magical circle.
        """
        return ((self._MagicClass__radius ** 2) * math.pi)
    
    def circumference(self):
        """Calculate and Return circumference of magical circle.

        Returns:
            float: Circumference of magical circle.
        """
        return (2 * math.pi * self._MagicClass__radius)
