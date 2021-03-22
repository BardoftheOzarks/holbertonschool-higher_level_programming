#!/usr/bin/python3
'''Let's write a json dictionary'''


def class_to_json(obj):
    '''makes dictionary of a json'''
    import json
    return obj.__dict__
