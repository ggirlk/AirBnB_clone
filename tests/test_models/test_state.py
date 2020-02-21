#!/usr/bin/python3
import unittest


from models.base_model import BaseModel
from models.state import State
'''test module for State class'''


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class
    """
     def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.state.name, "")
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertFalse(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "id"))
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

if __name__ == "__main__":
    main()
