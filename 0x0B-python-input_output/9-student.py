#!/usr/bin/python3
'''9-student.py Module'''


class Student:
    '''Define student calss'''
    def __init__(self, first_name, last_name, age):
        """Instaniation of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of student"""
        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
        return json_dict
