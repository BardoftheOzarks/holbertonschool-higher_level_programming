#!/usr/bin/python3
'''Creates subsubclass Square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class of Rectangle'''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        '''size functions for both width and height'''
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
