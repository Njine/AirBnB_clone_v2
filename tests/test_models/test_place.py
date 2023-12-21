#!/usr/bin/python3
"""Test for Place"""

import unittest
import os
from os import getenv
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """Test suite for the Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "4321-dcba"
        cls.place.name = "Death Star"
        cls.place.description = "UNLIMITED POWER!!!!!"
        cls.place.number_rooms = 1000000
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 607360
        cls.place.price_by_night = 10
        cls.place.latitude = 160.0
        cls.place.longitude = 120.0
        cls.place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.place

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring_Place(self):
        """Check for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_Place(self):
        """Check if Place has attributes"""
        attributes = [
            'id', 'created_at', 'updated_at', 'city_id', 'user_id', 'name',
            'description', 'number_rooms', 'number_bathrooms', 'max_guest',
            'price_by_night', 'latitude', 'longitude', 'amenity_ids'
        ]
        for attribute in attributes:
            self.assertTrue(hasattr(self.place, attribute))

    def test_is_subclass_Place(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attribute_types_Place(self):
        """Test attribute types for Place"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Place(self):
        """Test if save works"""
        original_created_at = self.place.created_at
        self.place.save()
        self.assertNotEqual(original_created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """Test if to_dict method works"""
        self.assertTrue('to_dict' in dir(self.place))


if __name__ == "__main__":
    unittest.main()
