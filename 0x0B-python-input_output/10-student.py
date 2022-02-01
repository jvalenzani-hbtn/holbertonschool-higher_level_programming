#!/usr/bin/python3
""" Student calss extension """

class Student:
    """ Student calss extension """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if(len(attrs) > 0):
            if(not attrs):
                new_dict = self.__dict__
            else:
                for k,v in self.__dict__.items():
                    if (k in attrs):
                        new_dict[k] = v
        return new_dict