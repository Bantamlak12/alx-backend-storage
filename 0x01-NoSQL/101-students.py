#!/usr/bin/env python3
"""
File: 101-students.py

Function:
--------
def top_students(mongo_collection):
A function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    parameters:
    - mongo_collection: pymongo collection object

    Returns:
    - All students sorted by average score
    """
    pipeline = [
            {
                "$group":
                    {"name": "$name",
                     "averageScore": {"$avg": "$topics.score"}
                     }
            },
            {"$sort": {"averageScore": -1}}
       ]

    return mongo_collection.aggregate(pipeline)
