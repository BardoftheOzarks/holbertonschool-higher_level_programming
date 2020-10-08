#!/usr/bin/python3
'''Read a file'''


def read_file(filename=""):
    f = open(filename)
    print(f.read())
