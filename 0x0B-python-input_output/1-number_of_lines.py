#!/usr/bin/python3
'''Count them lines'''


def number_of_lines(filename=""):
    f = open(filename)
    line = 0
    for chr in f.read():
        if chr is '\n':
            line += 1
    return line
