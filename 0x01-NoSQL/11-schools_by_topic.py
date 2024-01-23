#!/usr/bin/env python3
"""
File: 11-schools_by_topic.py

Function:
--------
A function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    parameters:
    - mono_collaction: pymongo collection object
    - topics (string) Topic to be searched
    """
    return mongo_collection.find({"topics": topics})
