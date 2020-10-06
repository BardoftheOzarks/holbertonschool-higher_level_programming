#!/usr/bin/python3
'''Creates class MyList'''


class MyList(list):
    '''subclass of list'''
    def print_sorted(self):
        print(sorted(self))
