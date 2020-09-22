#!/usr/bin/python3
'''Creates a class with a single attribute that returns square'''


class Square:
    '''A class with a single private instance attribute "size"'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = size

    def area(self):
        return self._Square__size**2
