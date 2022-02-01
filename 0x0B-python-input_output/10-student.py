#!/usr/bin/python3
""" Student calss extension """

st = __import__('9-student').Student

class Student(st):
    """ Student calss extension """

    def to_json(self, attrs=None):
        new_dict = {}
        for k,v in self.__dict__.items():
            if (attrs and k in attrs) or not attrs:
                new_dict[k] = v
        return new_dict