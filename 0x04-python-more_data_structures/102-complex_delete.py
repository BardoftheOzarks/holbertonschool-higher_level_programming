#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keyring = sorted(a_dictionary.keys())
        for key in keyring:
            if a_dictionary[key] == value:
                a_dictionary.pop(key)
    return a_dictionary
