#!/usr/bin/python3
'''Creates subsubclass Square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator('size', size)
        '''self._Rectangle__width = size
        self._Rectangle__height = size'''
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def _Rectangle__width(self):
        return self.__size

    @property
    def _Rectangle__height(self):
        return self.__size
