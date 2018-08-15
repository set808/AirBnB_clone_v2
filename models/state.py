#!/usr/bin/python3
'''
    Implementation of the State class
'''
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade='delete', backref='state')
    else:
        name = ''

        @property
        def cities(self):
            my_cities = models.storage.all(models.classes['City']).values()
            print(my_cities)
            return [city for city in my_cities if city.state_id == self.id]
