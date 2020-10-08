#!/usr/bin/python3
'''Let's write to a file'''


def write_file(filename='', text=''):
    with open(filename, 'w') as f:
        count = f.write(str(text))
        return count
