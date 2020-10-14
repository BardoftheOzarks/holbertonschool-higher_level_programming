#!/usr/bin/python
'''Unittest for Base class'''

import unittest
import Base from models.base
import Rectangle from models.base


class Test_Base(unittest.TestCase):
    '''test cases for Base class'''
    def test_base_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    '''def test_to_json_string(self):
        '''test cases for to_json_string'''
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        '''
