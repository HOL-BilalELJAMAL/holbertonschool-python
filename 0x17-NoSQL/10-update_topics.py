#!/usr/bin/env python3
"""
10-update_topics.py
Module that defines a function that changes all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document
    based on the name

    Args:
        mongo_collection (list): pymongo collection object
        name (str): Name of the school
        topics (list): List of topics
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
