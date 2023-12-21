#!/usr/bin/python3
"""Test for City"""

import unittest
import os
from os import getenv
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """Test suite for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.city

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring_City(self):
        """Check for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Check if City has attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'state_id', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.city, attribute))

    def test_is_subclass_City(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types_City(self):
        """Test attribute types for City"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """Test if save works"""
        original_created_at = self.city.created_at
        self.city.save()
        self.assertNotEqual(original_created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test if to_dict method works"""
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()
