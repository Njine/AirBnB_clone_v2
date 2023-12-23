#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import ForeignKeyConstraint

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
    ForeignKeyConstraint(['state_id'], ['states.id'])
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
