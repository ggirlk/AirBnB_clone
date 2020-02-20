#!/usr/bin/python3
""" base model for all other classes"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    class that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        init method
        """
        if args:
            pass
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        a = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(value, a))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
