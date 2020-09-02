#!/usr/bin/python3
def uppercase(str):
    newstring = ''
    for char in (str):
        c = ord(char)
        if c > 96 and c < 123:
            newstring += chr(c - 32)
        else:
            newstring += chr(c)
    print('{}'.format(newstring))
