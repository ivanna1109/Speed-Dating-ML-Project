from pymongo import MongoClient
import random
#import data_processing as dp

# Konekcija na MongoDB
def connect_to_db(col_name = 'mlPersonData'):
    client = MongoClient('mongodb://nastava.is.pmf.uns.ac.rs:27017/')
    db = client['databases']
    if (col_name == 'mlPersonData'):
        collection = db['mlPersonData']
    else:
        collection = db['mlRegisterUser']
    return collection

def check_user(username, password):
    collection = connect_to_db('mlRegisterUser')
    query = {"username": username, 'password': password}
    user = collection.find_one(query)
    if (user == None):
        return -1
    return user['userID']

#in the system cant be 2 users with the same username
def check_for_existing_username(username):
    collection = connect_to_db('mlRegisterUser')
    query = {"username": username}
    user = collection.find_one(query)
    if (user == None):
        return 0
    return 1

def register_user(userID, username, password):
    collection = connect_to_db('mlRegisterUser')
    new_user = {
        'userID': userID,
        'username': username,
        'password': password 
    }
    collection.insert_one(new_user)

def get_all_persons():
    collection = connect_to_db()
    persons = list(collection.find())
    #random.shuffle(persons)

    return persons

def find_person_by_ID(userID):
    persons = connect_to_db()
    query = {'userID': userID}
    person = persons.find_one(query)
    if (person == None):
        return None
    return person

def find_top_matches(list):
    top_matches = []
    persons = connect_to_db()
    for iid in list:
        query = {'iid': iid}
        person = persons.find_one(query)
        top_matches.append(person)
    return top_matches

def get_all_users():
    collection = connect_to_db('mlRegisterUser')
    return collection.find()
    
def insert_persons(data_reduced):
    collection = connect_to_db()
    persons_list = []
    for index, person in data_reduced.iterrows():
        person_doc = {
    'userID':index, 'iid': person['iid'], 'gender':person['gender'], 'age':person['age'], 
    'race': person['race'], 'race_str': '', 'field':person['field'], 'field_cd': person['field_cd'], 
    'imprace': person['imprace'], 'imprelig':person['imprelig'],'career':person['career'], 'career_c':person['career_c'],
    'income':person['income'], 'goal':person['goal'], 'date':person['date'], 'go_out':person['go_out'], 
    'sports':person['sports'], 'tvsports':person['tvsports'], 'exercise':person['exercise'], 
    'dining':person['dining'], 'museums':person['museums'], 'art':person['art'],'hiking':person['hiking'], 
    'gaming':person['gaming'], 'clubbing':person['clubbing'], 'reading':person['reading'], 'tv':person['tv'],
    'theater':person['theater'], 'movies':person['movies'], 'concerts':person['concerts'], 'music':person['music'],
    'shopping':person['shopping'], 'yoga':person['yoga'], 'attr1_1':person['attr1_1'], 'sinc1_1':person['sinc1_1'],
    'intel1_1':person['intel1_1'], 'fun1_1':person['fun1_1'], 'amb1_1':person['amb1_1'], 'shar1_1':person['shar1_1'],
    'attr3_1':person['attr3_1'], 'sinc3_1':person['sinc3_1'], 'intel3_1':person['intel3_1'], 
    'fun3_1':person['fun3_1'], 'amb3_1':person['amb3_1']
        }
        persons_list.append(person_doc)
    collection.insert_many(persons_list)


def update_type():
    collection = connect_to_db()
    persons = collection.find()
    for document in persons:
        current_value = document['amb3_1']
        new_value = int(current_value)  # Konvertujemo trenutnu vrijednost u int
        collection.update_one({'_id': document['_id']}, {'$set': {'amb3_1': new_value}})
    print('uspesno')

"""
update_type()

def add_persons():
    data = dp.read_data()
    data_reduced = dp.extract_attributes(data)
    data_of_person = dp.attributes_of_person(data_reduced)
    insert_persons(data_of_person)
    print("Uspesno!")

def update_race(idr, name):
    collection = connect_to_db()
    # Definisanje upita za ažuriranje
    filter = {"race": idr}
    # Definisanje nove vrednosti za atribut2
    update = {"$set": {"race_str": name}}

    # Ažuriranje dokumenata koji zadovoljavaju upit
    result = collection.update_many(filter, update)
    print("Uspesno")
"""
#register_user(8356, 'person8356', '12345')
#add_persons() #persons succesfully added to MongoDB
#update_race(6, 'Other')
