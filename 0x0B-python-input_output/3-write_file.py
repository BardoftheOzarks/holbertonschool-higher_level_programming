#!/usr/bin/python3
'''Let's write to a file'''


def write_file(filename='', text=''):
    with open(filename, 'w') as f:
        f.write(str(text))
