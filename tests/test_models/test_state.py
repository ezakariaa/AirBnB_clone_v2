#!/usr/bin/python3
"""
Unittest for State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Defines test cases for the State class."""

    def setUp(self):
        """Set up for the tests."""
        self.state_1 = State()

    def test_instance(self):
        """Test if state_1 is an instance of State."""
        self.assertIsInstance(self.state_1, State)

    def test_attributes(self):
        """Test if State has the correct attributes."""
        self.assertTrue(hasattr(self.state_1, "name"))

    def test_attribute_types(self):
        """Test the type of State attributes."""
        self.assertIsInstance(self.state_1.name, str)


if __name__ == '__main__':
    unittest.main()
