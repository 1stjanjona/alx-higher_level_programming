#!/usr/bin/python3
"""models/square.py Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class by Rectangle inheritance'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Overload __str__ method'''
        sqr = type(self).__name__
        id_ = self.id
        x_ = self.x
        y_ = self.y
        w = self.width
        return ('[{}] ({}) {}/{} - {}'.format(sqr, id_, x_, y_, w))

    @property
    def size(self):
        '''Getter of Square size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter of Square size to same value'''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Private instance of Square class by *args & **kwargs"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Update of Square Class by adding public attributes'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Return represented Wquare class'''
        i_d = self.id
        s = self.width
        x_ = self.x
        y_ = self.y
        return {"id": i_d, "size": s, "x": x_, "y": y_}
