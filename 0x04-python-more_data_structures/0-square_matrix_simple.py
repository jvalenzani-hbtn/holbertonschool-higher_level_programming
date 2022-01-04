#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_m = []
    for line in matrix:
        new_line = list(map(lambda x : x*x, line))
        new_m.append(new_line)
    return new_m