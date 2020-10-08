#!/usr/bin/python3
'''Count them lines'''


def number_of_lines(filename=""):
    '''returns number of lines in a file'''
    with open(filename) as f:
        line = 0
        for chr in f.read():
            if chr is '\n':
                line += 1
        return line
