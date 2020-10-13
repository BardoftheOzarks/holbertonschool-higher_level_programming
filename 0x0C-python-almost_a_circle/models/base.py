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
        with open('{}.json'.format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''translates json object to a string'''
        import json
        string_list = json.loads(json_string)
        if string_list is None or len(string_list) == 0:
            return []
        return string_list

    @classmethod
    def create(cls, **dictionary):
        '''creates an instance from a dictionary'''
        if cls.__name__ is 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Creates a list of instances from a file'''
        insta_list = []
        try:
            with open('{}.json'.format(cls.__name__)) as f:
                for obj in cls.from_json_string(f.read()):
                    insta_list.append(cls.create(**obj))
        except Exception:
            pass
        return insta_list
