#!/usr/bin/python3
'''Prints a text file'''


def text_indentation(text):
    '''Prints text and inserts two new lines after periods, question mark,
    and colons'''
    if type(text) is not str:
        raise TypeError('text must be a string')
    prev = ''
    for char in text:
        if char in ['.', '?', ':']:
            print(char, end='\n\n')
            prev = '\n'
        elif char is ' ' and prev in ['\n', '']:
            pass
        else:
            print(char, end='')
            prev = char
