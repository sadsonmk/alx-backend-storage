#!/usr/bin/env python3
"""is a module for a Python function that returns
    the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """a function that returns a list of school for a specific topic"""
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
