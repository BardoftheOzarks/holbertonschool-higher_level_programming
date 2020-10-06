#!/usr/bin/python3
'''Creates a not-quite-empty class'''


class BaseGeometry:
    '''practically empty class'''
    def area(self):
        raise Exception('area() is not implemented')
