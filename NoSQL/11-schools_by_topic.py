#!/usr/bin/env python3
""" Module 11-schools_by_topic: find schools by topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search

    Returns:
        List of documents with the given topic
    """
    return list(mongo_collection.find({ "topics": topic }))
