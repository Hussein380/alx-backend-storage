#!/usr/bin/env python3
''' Task 9 module
'''


def insert_school(mongo_collection, **kwargs):
    '''


    '''

    # Insert the document into the collection and get the result object
    result = mongo_collection.insert_one(kwargs)

    # Return the _id of newly inserdted document
    return result.inserted_id
