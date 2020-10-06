#!/usr/bin/python3
'''Function to check class'''


def inherits_from(obj, a_class):
    '''Returns True/False if obj is a subclass of a_class'''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
