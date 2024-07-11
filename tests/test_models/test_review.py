#!/usr/bin/python3
"""
Unittest for Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Defines test cases for the Review class."""
    
    def setUp(self):
        """Setup for Review tests."""
        self.review_1 = Review()
        
    def test_instance(self):
        """Test if the object is an instance of Review."""
        self.assertIsInstance(self.review_1, Review)
        
    def test_attributes(self):
        """Test Review attributes."""
        self.assertTrue(hasattr(self.review_1, "text"))
        self.assertTrue(hasattr(self.review_1, "place_id"))
        self.assertTrue(hasattr(self.review_1, "user_id"))
        
if __name__ == '__main__':
    unittest.main()
