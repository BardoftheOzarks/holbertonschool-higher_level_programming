#!/usr/bin/python3
'''Function to check class'''


def is_kind_of_class(obj, a_class):
    '''Returns True/False if obj is of type a_class or subclass thereof'''
    return issubclass(type(obj), a_class)
