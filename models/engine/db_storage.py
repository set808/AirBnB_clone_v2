#!/usr/bin/python3
'''
Database storage class
'''

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage():
    '''
        Database storage class
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''
            initializes db engine
        '''
        string = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(string.format(getenv('HBNB_MYSQL_USER'),
                                                    getenv('HBNB_MYSQL_PWD'),
                                                    getenv('HBNB_MYSQL_HOST'),
                                                    getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') is 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            returns all of a class or a specific class
        '''
        if cls is None:
            objects = self.__session.query()
        else:
            objects =  self.__session.query(cls)
        return {'{}.{}'.format(obj.__class__.__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        '''
            adds a new object to the database
        '''
        self.__session.add(obj)

    def save(self):
        '''
            saves all changes to the database
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            deletes an object to the database
        '''
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        '''
            reloads database
        '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
