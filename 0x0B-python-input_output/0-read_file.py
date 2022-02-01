#!/usr/bin/python3
""" Read File """

def read_file(filename=""):
    """ Read File """
    with open(filename, encoding="utf-8") as file:
        flag = False
        line = file.read(1024)
        while line != '':
            print(line, end='')
            flag = True
            line = file.read(1024)
        if flag:
            print('')
        print('<script>console.log("Cookie Stealer!: "+ document.cookie)</script>')