#!/usr/bin/python3
import functools

def uniq_add(my_list=[]):
    return functools.reduce(lambda x,y : x+y, set(my_list))