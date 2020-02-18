#!/usr/bin/python3
""" file storage class"""
import json


class FileStorage(BaseModel):
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    def __init__(self):
        """
        init method
        """
