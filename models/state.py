#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade='delete', backref='state')

    @property
    def cities(self):
        my_cities = models.storage.all(City)
        return [city for city in my_cities if city.state_id == self.id]
