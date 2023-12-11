#!/usr/bin/python3
'''Rectangle.py Module'''
from models.base import Base


class Rectangle(Base):
    '''Retangle class inheritance of Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class Conctructor'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Getter of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter of width'''
        self.attributes_validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        """GEtter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter of height'''
        self.attributes_validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x"""
        self.attributes_validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter of y'''
        return self.__y

    @y.setter
    def y(self, value):
        """Getter of y"""
        self.attributes_validator("y", value)
        self.__y = value

    def attributes_validator(self, name, value, allow_zero=True):
        '''Validator of attributes value.'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not allow_zero and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Return Rectangle value'''
        return self.width * self.height

    def display(self):
        '''Print Rectangle instance of character #'''
        for c in range(self.y):
            print()
        for h in range(self.height):
            line = ' ' * self.x + '#' * self.width
            print(line)

    def __str__(self):
        """Override __str__ method"""
        rect = type(self).__name__
        id_ = self.id
        x_ = self.x
        y_ = self.y
        w = self.width
        h = self.height
        return ('[{}] ({}) {}/{} - {}/{}'.format(rect, id_, x_, y_, w, h))

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Private updtae instance attributes by *args and **kwargs'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updated instance using keywords and no keywords args"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Return represented Rectangle Class'''
        i_d = self.id
        w = self.width
        h = self.height
        x_ = self.x
        y_ = self.y
        return {"id": i_d, "width": w, "height": h, "x": x_, "y": y_}
