#!/usr/bin/python3
'''Let's write to a file'''


def append_write(filename='', text=''):
    '''appends text to filename'''
    with open(filename, 'a') as f:
        count = f.write(str(text))
        return count
