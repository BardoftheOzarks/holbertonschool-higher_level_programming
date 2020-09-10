#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keyring = sorted(a_dictionary.keys())
    for key in keyring:
        print('{}: {}'.format(key, a_dictionary[key]))
