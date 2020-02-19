#!/usr/bin/python3
"""
Module for init.py
"""
from models.engine import file_storage


"""
creates an instance from FileStorage and reloads it
"""
storage = file_storage.FileStorage()
storage.reload()
