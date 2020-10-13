#!/usr/bin/python3
'''Because you know I'm all about that Base'''


class Base:
    '''Base class of all other classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Makes a json string from a dictionary'''
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves json list to a file'''
        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        dictionaries = []
        for obj in list_objs:
            dictionaries.append(obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(cls.to_json_string(dictionaries))

'''    @staticmethod
    def from_json_string(json_string):
        import json
        
        if json.dumps(json_string) is None or json.dumps(json)
'''
