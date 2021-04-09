#!/usr/bin/python3
'''Finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    '''And away we go!'''
    if not list_of_integers:
        return None
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
    for x in range(len(list_of_integers) - 1):
        if not list_of_integers[x - 1] or \
           list_of_integers[x] > list_of_integers[x - 1]:
            if not list_of_integers[x + 1] or \
               list_of_integers[x] > list_of_integers[x + 1]:
                return list_of_integers[x]
    return list_of_integers[0]
