#!/usr/bin/python3
"""Test for Amenity"""

import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.amenity

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring_Amenity(self):
        """Check for docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Check if Amenity has attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.amenity, attribute))

    def test_is_subclass_Amenity(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute_types_Amenity(self):
        """Test attribute types for Amenity"""
        self.assertIsInstance(self.amenity.name, str)

    def test_save_Amenity(self):
        """Test if save works"""
        original_created_at = self.amenity.created_at
        self.amenity.save()
        self.assertNotEqual(original_created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Test if to_dict method works"""
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
