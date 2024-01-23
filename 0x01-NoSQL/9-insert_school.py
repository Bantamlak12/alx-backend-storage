#!/usr/bin/env python3
"""
File: 9-insert_school.py

Function:
--------
def insert_school(mongo_collection, **kwargs):
A function that inserts a new document in a collaction based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    parameters:
    - mongo_collection: pymongo collection object

    Returns:
    - new _id
    """
    for key, value in kwargs.items():
        mongo_collection.insert_one({key: value})

