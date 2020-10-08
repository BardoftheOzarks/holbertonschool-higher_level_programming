#!/usr/bin/python3
'''Let's decrypt'''


def load_from_json_file(filename):
    '''turns json file into a string'''
    import json
    with open(filename) as f:
        return json.load(f)
