#!/usr/bin/env python3
"""
8-all.py
Module that defines a function that lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection

    Args:
        mongo_collection (list): pymongo collection object
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
