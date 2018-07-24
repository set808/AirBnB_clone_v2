#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import unittest
from models.base_model import BaseModel, Base
from models.state import State
from os import getenv


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'State only inherits from Base when using db')
    def test_State_inheritence_db(self):
        '''
            Test that State class inherits from Base
        '''
        new_state = State()
        self.assertIsInstance(new_state, Base)

    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attributes are NoneType in db')
    def test_State_attributes_type_fs(self):
        '''
            Test that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'testing if attribute stores to db')
    def test_State_attributes_store_db(self):
        '''
            Test is no name stores to db
        '''
        new = State()
        with self.assertRaises(Exception):
            new.save()
