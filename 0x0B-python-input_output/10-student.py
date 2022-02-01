#!/usr/bin/python3
""" Student calss extension """

class Student:
    """ Student calss extension """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if(attrs == None):
            return(self.__dict__)
        new_dict = {}
        for k,v in self.__dict__.items():
            if (k in attrs):
                new_dict[k] = v
        return new_dict