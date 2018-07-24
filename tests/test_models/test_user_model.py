#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel, Base
from models.user import User
from io import StringIO
import sys
import datetime
from os import getenv


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'User only inherits from Base when using db')
    def test_User_inheritence_db(self):
        '''
            Test that State class inherits from Base
        '''
        new_user = User()
        self.assertIsInstance(new_user, Base)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attribute is not string when using db storage')
    def test_type_email_fs(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'testing if attribute stores to db')
    def test_store_email_db(self):
        '''
            Test if email stores correctly
        '''
        new = User(password='pass')
        with self.assertRaises(Exception):
            new.save()

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'testing if attribute stores to db')
    def test_store_password_db(self):
        '''
            Test if password stores correctly
        '''
        new = User(email='email@email.com')
        with self.assertRaises(Exception):
            new.save()

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attribute is not string when using db storage')
    def test_type_first_name_fs(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attribute is not string when using db storage')
    def test_type_last_name_fs(self):
        '''
            Test the type of last_name
        '''
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attribute is not string when using db storage')
    def test_type_password_fs(self):
        '''
            Test the type of password
        '''
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
