#!/usr/bin/python3
'''base.py Module'''
import json
import csv


class Base:
    '''Manage id attribute in all future classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Class Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return def to_json_string(list_dictionaries)'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Return list of JSON string representation json_string'''
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Write JSON string representation of list_objs to a file'''
        if list_objs is not None:
            for obj in list_objs:
                list_objs = [obj.to_dictionary()]
        else:
            list_objs = []
        filename = ('{}.json'.format(cls.__name__))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Return dummy instance (Rectangle or Square)'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Return list of instances'''
        from os import path
        files = ('{}.json'.format(cls.__name__))
        if not path.isfile(files):
            return []
        with open(files, 'r', encoding="utf-8") as f:
            for dctnr in cls.from_json_string(f.read()):
                return [cls.create(**dctnr)]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Save file to csv'''
        from models.rectangle import Rectangle
        from models.square import Square
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    if isinstance(obj, Rectangle):
                        obj_l = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif isinstance(obj, Square):
                        obj_l = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(obj_l)

    @classmethod
    def load_from_file_csv(cls):
        '''Load csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        obj_list = []
        filename = cls.__name__ + ".csv"
        with open(filename, "r", newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls.__name__ is Rectangle:
                    i = row[0]
                    w = row[1]
                    h = row[2]
                    a = row[3]
                    b = row[4]
                    c = {"id": i, "Width": w, "height": h, "x": a, "y": b}
                elif cls.__name__ is Square:
                    i = row[0]
                    s = row[1]
                    n = row[2]
                    m = row[3]
                    c = {"id": i, "size": s, "x": n, "y": m}
                obj_list.append(cls.create(**c))
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Open widow and draws of Rectangle and Square'''
        import turtle
        import time
        from random import randrange
        turtle.Screen().coloemode(255)
