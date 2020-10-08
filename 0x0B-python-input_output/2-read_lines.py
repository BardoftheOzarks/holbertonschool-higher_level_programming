#!/usr/bin/python3
'''Read some lines'''


def read_lines(filename="", nb_lines=0):
    '''How many lines do you want'''
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read())
        for i in range(nb_lines):
            print(f.readline(), end='')
