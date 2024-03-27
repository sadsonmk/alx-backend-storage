#!/usr/bin/env python3
"""a module for a Python function that inserts a new
    document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """a function that inserts a new document in
    a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
