#!/usr/bin/python3
"""
Unittest for Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines test cases for the Amenity class."""
    
    def setUp(self):
        """Setup for Amenity tests."""
        self.amenity_1 = Amenity()
        
    def test_instance(self):
        """Test if the object is an instance of Amenity."""
        self.assertIsInstance(self.amenity_1, Amenity)
        
    def test_attributes(self):
        """Test Amenity attributes."""
        self.assertTrue(hasattr(self.amenity_1, "name"))
        
if __name__ == '__main__':
    unittest.main()
