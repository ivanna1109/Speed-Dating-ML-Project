from pymongo import MongoClient
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

def log_in(username, password):
    collection = connect_to_db('mlRegisterUser')
    query = {"username": username, 'password': password}
    user = collection.find_one(query)
    if (user == None):
        return 0
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
    return list(collection.find())

def find_person_by_ID(userID):
    persons = connect_to_db()
    query = {'userID': userID}
    person = persons.find_one(query)
    if (person == None):
        return None
    return person

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
    'attr2_1':person['attr2_1'], 'sinc2_1':person['sinc2_1'], 'intel2_1':person['intel2_1'], 
    'fun2_1':person['fun2_1'], 'amb2_1':person['amb2_1'], 'shar2_1':person['shar2_1'],
        }
        persons_list.append(person_doc)
    collection.insert_many(persons_list)

"""
def update_type():
    collection = connect_to_db()
    persons = collection.find()
    for document in persons:
        current_value = document['career_c']
        new_value = int(current_value)  # Konvertujemo trenutnu vrijednost u int
        collection.update_one({'_id': document['_id']}, {'$set': {'career_c': new_value}})
    print('uspesno')

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

#register_user(9000, 'ivanna', 'test')
#add_persons() #persons succesfully added to MongoDB
update_race(6, 'Other')

persons = list(get_all_persons())
print(type(persons))
persons = persons[:10]
print(len(persons))
"""