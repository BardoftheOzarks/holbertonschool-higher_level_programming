#!/usr/bin/python3
'''Read a file'''


def read_file(filename=""):
    with open(filename) as f:
        print(f.read())
