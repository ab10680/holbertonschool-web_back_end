#!/usr/bin/env python3
""" Module 8-all: list all documents in a collection """


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents, or empty list if no documents exist
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
