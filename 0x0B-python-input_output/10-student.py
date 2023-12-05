#!/usr/bin/python3
'''10-student.py Module'''


class Student:
    def __init__(self, first_name, last_name, age):
        """Instaniation of student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        json_dict = {}
        if attrs is not None and isinstance(attrs, list):
            for key, value in self.__dict__.items():
                is_instance = isinstance(value, (list, dict, str, int, bool))
                if key in attrs and is_instance:
                    json_dict[key] = value
        else:
            for key, value in self.__dict__.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[key] = value
        return json_dict
