#!/usr/bin/python3
'''Creates a Rectangle class'''


class Rectangle:
    '''A class with height and width'''
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        return self._Rectangle__width

    @property
    def height(self):
        return self._Rectangle__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._Rectangle__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._Rectangle__height = value

    def area(self):
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        return ((self._Rectangle__height + self._Rectangle__width) * 2)
