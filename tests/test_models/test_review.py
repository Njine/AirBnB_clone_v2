#!/usr/bin/python3
"""Test for Review"""

import unittest
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Test suite for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The strongest in the Galaxy"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.rev

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring_Review(self):
        """Check for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_Review(self):
        """Check if Review has attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'place_id', 'text', 'user_id']
        for attribute in attributes:
            self.assertTrue(hasattr(self.rev, attribute))

    def test_is_subclass_Review(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attribute_types_Review(self):
        """Test attribute types for Review"""
        self.assertIsInstance(self.rev.text, str)
        self.assertIsInstance(self.rev.place_id, str)
        self.assertIsInstance(self.rev.user_id, str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """Test if save works"""
        original_created_at = self.rev.created_at
        self.rev.save()
        self.assertNotEqual(original_created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """Test if to_dict method works"""
        self.assertTrue('to_dict' in dir(self.rev))


if __name__ == "__main__":
    unittest.main()
