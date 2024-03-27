#!/usr/bin/env python3
"""a module for a Python function that changes
    all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """a function that changes all topics of
        a school document based on name"""
    mongo_collection.update_many({"name": name}, {'$set': {'topics': topics}})
