#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class TestCity(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_City_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'City only inherits from Base when using db')
    def test_City_inheritance_db(self):
        '''
            tests that the City class Inherits from Base
        '''
        new_city = City()
        self.assertIsInstance(new_city, Base)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attributes are NoneType in db')
    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attributes are NoneType in db')
    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
