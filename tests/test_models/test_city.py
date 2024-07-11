#!/usr/bin/python3
"""
Unittest for City
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Defines test cases for the City class."""
    
    def setUp(self):
        """Setup for City tests."""
        self.city_1 = City()
        
    def test_instance(self):
        """Test if the object is an instance of City."""
        self.assertIsInstance(self.city_1, City)
        
    def test_attributes(self):
        """Test City attributes."""
        self.assertTrue(hasattr(self.city_1, "state_id"))
        self.assertTrue(hasattr(self.city_1, "name"))
        
if __name__ == '__main__':
    unittest.main()
