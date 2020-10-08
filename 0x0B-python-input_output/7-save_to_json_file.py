#!/usr/bin/python3
'''Let's drop the s'''


def save_to_json_file(my_obj, filename):
    '''dumps to a file'''
    import json
    json.dump(my_obj, filename)
