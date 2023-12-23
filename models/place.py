#!/usr/bin/python3
"""This is the Place class."""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.base_model import BaseModel, Base

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Class for representing places.

    Attributes:
        city_id (str): City ID.
        user_id (str): User ID.
        name (str): Name input.
        description (str): String description.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Maximum guests.
        price_by_night (int): Price for staying.
        latitude (float): Latitude.
        longitude (float): Longitude.
        amenity_ids (list): List of Amenity IDs.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns a list of reviews related to the place."""
            reviews_list = [model for model in models.storage.all().values()
                            if isinstance(model, Review) and model.place_id == self.id]
            return reviews_list

        @property
        def amenities(self):
            """Returns a list of amenity ids."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity ids to the attribute."""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
