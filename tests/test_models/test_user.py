#!/usr/bin/python3

"""UserModel test suite"""
import unittest
import datetime
from models.user import User
from models.base_model import BaseModel


class TestUserModel(unittest.TestCase):
    """UserModel unit tests"""

    def test_User_inherits_from_BaseModel(self):
        """tests that User inherits from BaseModel"""
        user = User()
        self.assertEqual(issubclass(user.__class__, BaseModel), True)
