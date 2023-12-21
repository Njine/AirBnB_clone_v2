#!/usr/bin/python3
"""Test for State"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test suite for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.state

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_State(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring_State(self):
        """Check for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """Check if State has attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.state, attribute))

    def test_is_subclass_State(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attribute_types_State(self):
        """Test attribute type for State"""
        self.assertIsInstance(self.state.name, str)

    def test_save_State(self):
        """Test if save works"""
        original_created_at = self.state.created_at
        self.state.save()
        self.assertNotEqual(original_created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Test if to_dict method works"""
        self.assertTrue('to_dict' in dir(self.state))


if __name__ == "__main__":
    unittest.main()
