#!/usr/bin/python3
"""Test for BaseModel"""

import unittest
import os
from os import getenv
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.base

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring_BaseModel(self):
        """Check for docstrings"""
        docstrings = [
            BaseModel.__doc__,
            BaseModel.__init__.__doc__,
            BaseModel.__str__.__doc__,
            BaseModel.save.__doc__,
            BaseModel.to_dict.__doc__
        ]
        for docstring in docstrings:
            self.assertIsNotNone(docstring)

    def test_methods_BaseModel(self):
        """Check if BaseModel has methods"""
        methods = ['__init__', 'save', 'to_dict']
        for method in methods:
            self.assertTrue(hasattr(BaseModel, method))

    def test_init_BaseModel(self):
        """Test if the base is an instance of BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_BaseModel(self):
        """Test if save works"""
        original_created_at = self.base.created_at
        self.base.save()
        self.assertNotEqual(original_created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Test if to_dict method works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
