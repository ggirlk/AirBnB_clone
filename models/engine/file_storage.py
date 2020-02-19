#!/usr/bin/python3
""" file storage class"""
import json
from models.base_model import BaseModel

class FileStorage(BaseModel):
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """ returns the
        dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects
        to the JSON file
        """
        with open(self.__file_path, w, encoding="UTF-8") as my_file:
            new_dict={}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, my_file)

    def reload(self):
        """ deserializes the JSON
        file to __objects
        """
        if self.__file_path:
            with open(self.__file_path, r, encoding="UTF-8") as my_file:
                new_obj = json.load(my_file)
            for key, value in new_obj.items():
                class_name = value['__class__']
                del value['__class__']
                self.__objects[key] = eval(class_name)(**value)
