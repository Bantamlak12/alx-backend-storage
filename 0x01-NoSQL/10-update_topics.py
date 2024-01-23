#!/usr/bin/env python3
"""
File: 10-update_topics.py

Function:
---------
A function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    parameters:
    - mongo_collection: pymongo colection object
    - name (string): The school name to update
    - topicd (list of strings): List of topics approached in the school

    Returns:
    - Updated document
    """
    return mongo_collection.update_many(
            {name: name},
            {$set: {topics: topics}}
        )
