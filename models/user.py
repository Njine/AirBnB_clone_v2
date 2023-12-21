#!/usr/bin/python3
"""User Class Module"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """
    User class for representing users with specific attributes.

    Attributes:
        email (str): User's email address.
        password (str): User's login password.
        first_name (str): User's first name.
        last_name (str): User's last name.
        places (relationship): Relationship with Place class, cascade on delete.
        reviews (relationship): Relationship with Review class, cascade on delete.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
