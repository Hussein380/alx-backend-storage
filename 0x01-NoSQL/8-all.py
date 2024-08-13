#!/usr/bin/env python3
'''
Task 8 module
'''

def list_all(mongo_collection):
    '''
    list all documents collections
    Args:
        mongo_collection(pymongo.colection.collection): The pymongo
        collection object from which to list documents.
    Returns:
        list: A list of all documents in the collection
    '''
    # Retrieves all documents from collectionand conert them to a list
    return [doc for doc in mongo_collection.find()]
