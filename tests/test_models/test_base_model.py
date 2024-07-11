#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines test cases for the BaseModel class."""

    def test_instance(self):
        """Test instantiation of BaseModel object."""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))

    def test_id(self):
        """Test if id is unique."""
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_datetime(self):
        """Test created_at and updated_at are datetime objects."""
        model = BaseModel()
        self.assertTrue(isinstance(model.created_at, datetime))
        self.assertTrue(isinstance(model.updated_at, datetime))

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue("created_at" in model_dict)
        self.assertTrue("updated_at" in model_dict)
        self.assertTrue("id" in model_dict)
        self.assertTrue("__class__" in model_dict)

    def test_save(self):
        """Test save method updates 'updated_at'."""
        model = BaseModel()
        updated_at_before = model.updated_at
        model.save()
        updated_at_after = model.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)


if __name__ == '__main__':
    unittest.main()

