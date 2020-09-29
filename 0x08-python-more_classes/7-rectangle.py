#!/usr/bin/python3
'''Creates a Rectangle class'''


class Rectangle:
    '''A class with height and width'''
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        if self._Rectangle__height is 0 or self._Rectangle__width is 0:
            return 0
        return ((self._Rectangle__height + self._Rectangle__width) * 2)

    def __str__(self):
        sting = ''
        for h in range(self._Rectangle__height):
            for w in range(self._Rectangle__width):
                sting += str(self.print_symbol)
            if (h + 1) < self._Rectangle__height:
                sting += '\n'
        return sting

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self._Rectangle__width,
                                          self._Rectangle__height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
