#!/usr/bin/python3

def element_at(my_list, idx):
    ret = None
    if idx >= 0 and idx < len(my_list):
        ret = my_list[idx]
    return ret