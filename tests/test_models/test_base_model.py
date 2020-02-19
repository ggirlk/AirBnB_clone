#!/usr/bin/python3


"""BaseModel test suite"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """BaseModel unit tests"""

    def test_base_object_should_be_of_type_BaseModel(self):
        """tests that instances of BaseModel should be of type BaseModel"""
        model = BaseModel()
        self.assertEqual(type(model), BaseModel)

    def test_base_object_has_an_id(self):
        """tests that BaseModel objects have an id attribute"""
        model = BaseModel()
        self.assertEqual(model.id is None, False)
