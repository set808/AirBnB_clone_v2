#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from os import getenv


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'Amenity only inherits from Base when using db')
    def test_Amenity_inheritence_db(self):
        '''
            tests that the Amenity class Inherits from Base
        '''
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Base)

    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attributes are NoneType in db')
    def test_Amenity_attribute_type(self):
        '''
            Test that Amenity class had name attribute's type.
        '''
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'testing if attribute stores to db')
    def test_Amenity_attribute_store(self):
        '''
            Test if name stores correctly
        '''
        new_amenity = Amenity()
        with self.assertRaises(Exception):
            new_amenity.save()
