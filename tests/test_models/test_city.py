#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.city import City

'''test module for City class'''


class TestCity(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of city/json file'''
        self.city = City()

    def tearDown(self):
        '''method to tear down instance of city/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass
if __name__ == "__main__":
    main()
