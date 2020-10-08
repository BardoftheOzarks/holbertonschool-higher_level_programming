#!/usr/bin/python3
'''Read a file'''


def read_file(filename=""):
    '''reads a file and prints it'''
    with open(filename) as f:
        print(f.read(), end='')
