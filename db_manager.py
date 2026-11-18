import pymongo 

DB_NAME = "game"
DB_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")

def get_db():
    return DB_CLIENT[DB_NAME]

def fetch_collections(collection_name):
    db = get_db()
    collection = db.get_collection(collection_name)

    found = collection.find({})
    return found

def get_characters():
    return fetch_collections("characters")

def get_monsters():
    return fetch_collections("monsters")

def get_scores():
    return fetch_collections("scores")

def insert_new_score(score):
    db = get_db()
    db["scores"].insert_one(score)

def get_top_scores(limit):
    db = get_db()
    score_collection = db["scores"]
    top_scores = list(score_collection.find("score", pymongo.DESCENDING).limit(limit))
    return top_scores