from pymongo import MongoClient

def connect_to_db():
    # Konekcija na MongoDB
    client = MongoClient('mongodb://nastava.is.pmf.uns.ac.rs:27017/')
    db = client['databases']
    collection = db['mlPersonData']
    return collection
    
def insert_doc():
    collection = connect_to_db()
    print("Test")
    test_doc = {
        'test':'Ivana'
    }
    collection.insert_one(test_doc)