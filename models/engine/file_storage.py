#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        all: returns the dictionary of all objects
        """
        return FileStorage.__objects

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
        with open(self.__file_path, 'w', encoding="UTF-8") as my_file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, my_file)

    def reload(self):
        """ deserializes the JSON
        file to __objects
        """
        if os.path.isfile(self.__file_path):
            if os.stat(self.__file_path).st_size != 0:
                with open(self.__file_path, encoding='UTF-8') as my_file:
                    new_object = json.load(my_file)
                for key, value in new_object.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
