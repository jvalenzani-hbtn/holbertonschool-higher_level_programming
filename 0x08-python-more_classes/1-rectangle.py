#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError
        if w < 0:
            raise ValueError
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError
        if h < 0:
            raise ValueError
        self.__height = h