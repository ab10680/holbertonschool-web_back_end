#!/usr/bin/env python3
""" Module 9-insert_school: insert a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs representing document fields

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
