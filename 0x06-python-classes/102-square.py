#!/usr/bin/python3
'''Creates a class with a single attribute that returns square'''


class Square:
    '''A class with a single private instance attribute "size"'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size**2

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __lt__(self, other):
        if self.__size < other.__size:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__size > other.__size:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__size <= other.__size:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__size >= other.__size:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__size == other.__size:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__size != other.__size:
            return True
        else:
            return False
