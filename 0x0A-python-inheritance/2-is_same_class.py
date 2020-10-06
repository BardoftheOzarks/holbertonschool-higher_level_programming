#!/usr/bin/python3
'''Function to check class'''


def is_same_class(obj, a_class):
    '''Returns True/False if obj is of type a_class'''
    if type(obj) is a_class:
        return True
    else:
        return False
