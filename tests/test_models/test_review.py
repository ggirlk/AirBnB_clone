#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.review import Review

'''test module for Review class'''


class TestReview(unittest.TestCase):
    """
    TestReview class
    """
    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertFalse(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "id"))
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

if __name__ == "__main__":
    main()
