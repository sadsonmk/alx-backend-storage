#!/usr/bin/env python3
"""a module which contains a function to list all documents in a collection"""


def list_all(mongo_collection):
    """a function that lists all documents in a collection"""
    docs = mongo_collection.find()
    return list(docs)
