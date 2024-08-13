#!/usr/bin/env python3
'''Task 10's module.
'''

def update_topics(mongo_collection, name, topics):
    '''Updates the topics of a school document based on the name.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object where the document will be updated.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.
        
    Returns:
        None
    '''
    # Update all documents with the specified name by setting the 'topics' field
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
