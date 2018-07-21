#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''
    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if id not in kwargs:
            self.id = str(uuid.uuid4())
            needs_save = True
        else:
            needs_save = False
        if 'created_at' not in kwargs:
            self.created_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()
        else:
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")

        for key, val in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, val)
        if needs_save == True:
            models.storage.new(self)


    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
