#!/usr/bin/env python3
'''Task 11's module.
'''

def schools_by_topic(mongo_collection, topic):
    '''Returns the list of schools having a specific topic.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        topic (str): The topic to search for in the school documents.
        
    Returns:
        list: A list of dictionaries representing the schools that have the specified topic.
    '''
    # Create a filter to find documents where 'topics' contains the specified topic
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    # Return a list of documents that match the filter
    return [doc for doc in mongo_collection.find(topic_filter)]
