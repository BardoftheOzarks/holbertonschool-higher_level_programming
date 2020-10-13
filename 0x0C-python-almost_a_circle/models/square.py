#!/usr/bin/python3
'''And now, the Square!'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A square is a type of rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''Spell it out string style'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,\
                                                 self.width)

    @property
    def size(self):
        '''getter for private attribute size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for private attribute size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates values for a rectangle'''
        if args and len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.size = args[arg]
                if arg == 2:
                    self.x = args[arg]
                if arg == 3:
                    self.y = args[arg]
        else:
            for arg in kwargs:
                if arg == 'id':
                    self.id = kwargs[arg]
                if arg == 'size':
                    self.size = kwargs[arg]
                if arg == 'x':
                    self.x = kwargs[arg]
                if arg == 'y':
                    self.y = kwargs[arg]

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
