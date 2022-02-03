#!/usr/bin/python3

class Base:

    __nb_objects = 0
    
    def __init__(self, id=None):
        if(type(id) != int or not id):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def nb_objects(cls):
        return cls.__nb_objects