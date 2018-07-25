#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel, Base
from models.review import Review
from os import getenv


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     'Review only inherits from Base when using db')
    def test_Review_inheritance_db(self):
        '''
            tests that the Review class Inherits from Base
        '''
        new_review = Review()
        self.assertIsInstance(new_review, Base)

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                     'attributes are NoneType in db')
    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
