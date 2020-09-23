#!/usr/bin/python3
'''Creates a class with two attributes'''


class Square:
    '''A class with two private instance attributes'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) is not tuple or type(position[0]) is not int or\
           type(position[1]) is not int or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size is 0:
            print()
        for o in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for spaces in range(self.__position[0]):
                print(' ', end='')
            for hashes in range(self.__size):
                print('#', end='')
            print()

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or type(value[0]) is not int or\
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
