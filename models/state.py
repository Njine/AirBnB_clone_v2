#!/usr/bin/python3
"""This is the state class"""
import shlex
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all_objects = models.storage.all()
        city_list = []
        result = []

        for key in all_objects:
            city_key = key.replace('.', ' ')
            city_key = shlex.split(city_key)
            if city_key[0] == 'City':
                city_list.append(all_objects[key])

        for elem in city_list:
            if elem.state_id == self.id:
                result.append(elem)

        return result
