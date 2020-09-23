#!/usr/bin/python3
'''Makes a Magic class'''


class MagicClass:
    '''Stores a radius and computes either area
    or circumference of a circle'''

    def __init__(self, radius=0):

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass__radius**2 * pi

    def circumference(self):
        return 2 * math(pi) * self._MagicClass__radius
