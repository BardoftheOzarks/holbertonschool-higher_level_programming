#!/usr/bin/python3
'''Let's write to a file'''


def write_file(filename='', text=''):
    '''writes text to filename'''
    with open(filename, 'w') as f:
        count = f.write(str(text))
        return count
