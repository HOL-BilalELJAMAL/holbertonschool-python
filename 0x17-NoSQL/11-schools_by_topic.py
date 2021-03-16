#!/usr/bin/env python3
"""
11-schools_by_topic.py
Module that defines a function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school having a specific topic

    Args:
        mongo_collection (list): pymongo collection object
        topic (str): Topic name
    """
    return mongo_collection.find({"topics": topic})
