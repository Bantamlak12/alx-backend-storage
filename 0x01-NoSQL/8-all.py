#!/usr/bin/env python3
"""
File: 8-all.py

Function
-------
A function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    parameters:
    - mongo_collaction: pymongo collection object

    Returns:
    - Documents in a collaction or
    - Empty list if no document
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []
    else:
        return list(documents)

