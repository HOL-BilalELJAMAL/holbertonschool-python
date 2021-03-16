#!/usr/bin/env python3
"""
101-students.py
Module that defines a function that returns all students
sorted by average score
"""


def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score

    Args:
        mongo_collection (list): pymongo collection object
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
