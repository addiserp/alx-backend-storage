#!/usr/bin/env python3
"""
    a Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """
        a Python function that lists all documents in a collection:

    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
    
