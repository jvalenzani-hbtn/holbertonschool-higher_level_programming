#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        flag = False
        line = file.read(1024)
        while line != '':
            print(line, end='')
            flag = True
            line = file.read(1024)
        if flag:
            print('')