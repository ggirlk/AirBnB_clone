#!/usr/bin/python3
""" base model for all other classes"""
from  datetime import datetime
import uuid


class BaseModel:
    """
    class that defines all common attributes/methods
    for other classes
    """
    def __init__(self):
        """
        init method
        """
        self.id = str(uuid.uuid1())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
        return string

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
