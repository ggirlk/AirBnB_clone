#!/usr/bin/python3
""" file storage class"""
import json


class FileStorage(BaseModel):
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    def __init__(self, *args, **kwargs):
        """
        class constructor
        """

    @property
    def file_path(self):
        """ file_path getter """
        return (self.__file_path)

    @file_path.setter
    def file_path(self, value):
        """ file path setter """
        __file_path = value

    @property
    def objects(self):
        """ objects getter """
        return (self.__objects)

    @objects.setter
    def objects(self, value):
        """ objects setter """
        __objects = value

    def all(self):
        """ returns the 
        dictionary __objects
        """
        return (self.__objects)

    def new(self, obj): 
        """ sets in __objects the obj 
        with key <obj class name>.id
        """
        
    def save(self):
        """ serializes __objects
        to the JSON file
        """

    def reload(self):
        """ deserializes the JSON
        file to __objects
        """
