#!/usr/bin/python3
"""This is the User class."""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """Class for representing users.

    Attributes:
        email (str): Email address.
        password (str): Password for login.
        first_name (str): First name.
        last_name (str): Last name.
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
