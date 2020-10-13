#!/usr/bin/python3
'''Let's make a rectangle'''

from models.base import Base


class Rectangle(Base):
    '''It's a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        '''getter for private instance attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for private instance attribute width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''getter for private instance attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for private instance attribute height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''getter for private instance attribute x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for private instance attribute x'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''getter for private instance attribute y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for private instance attribute y'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''creates a visual representation of the rectangle'''
        for y in range(self.y):
            print()
        for row in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        '''defines the string representation of the rectangle'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,\
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''updates values for a rectangle'''
        if args and len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                if arg == 2:
                    self.height = args[arg]
                if arg == 3:
                    self.x = args[arg]
                if arg == 4:
                    self.y = args[arg]
        else:
            for arg in kwargs:
                if arg == 'id':
                    self.id = kwargs[arg]
                if arg == 'width':
                    self.width = kwargs[arg]
                if arg == 'height':
                    self.height = kwargs[arg]
                if arg == 'x':
                    self.x = kwargs[arg]
                if arg == 'y':
                    self.y = kwargs[arg]

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
