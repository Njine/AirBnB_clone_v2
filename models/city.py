#!/usr/bin/python3
"""City Module for HBNB project"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id (str): The state id.
        name (str): Input name.
        places (relationship): Relationship with Place class, cascade on delete.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship(
        "Place",
        cascade='all, delete, delete-orphan',
        backref="cities"
    )
