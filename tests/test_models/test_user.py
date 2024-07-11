#!/usr/bin/python3
"""
Unittest for User
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Defines test cases for the User class."""

    def setUp(self):
        """Set up for the tests."""
        self.user_1 = User()

    def test_instance(self):
        """Test if user_1 is an instance of User."""
        self.assertIsInstance(self.user_1, User)

    def test_attributes(self):
        """Test if user has the correct attributes."""
        self.assertTrue(hasattr(self.user_1, "email"))
        self.assertTrue(hasattr(self.user_1, "password"))
        self.assertTrue(hasattr(self.user_1, "first_name"))
        self.assertTrue(hasattr(self.user_1, "last_name"))

    def test_attribute_types(self):
        """Test the type of User attributes."""
        self.assertIsInstance(self.user_1.email, str)
        self.assertIsInstance(self.user_1.password, str)
        self.assertIsInstance(self.user_1.first_name, str)
        self.assertIsInstance(self.user_1.last_name, str)


if __name__ == '__main__':
    unittest.main()
