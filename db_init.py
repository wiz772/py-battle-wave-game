import pymongo
import models

DB_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DB_NAME = 'game'

def is_db_created():
    all_databases_name = DB_CLIENT.list_database_names()
    if DB_NAME in all_databases_name:
        return True
    return False

def create_db():
    # regarder si la db est déjà créer sinon la créer
    if not is_db_created():
    # créer les collections
        create_collections()
        print("DB Crée.")


def create_collections():
    # créer chaque collection
    create_monsters_collection()
    create_characters_collection()
    create_players_collection()

def create_monsters_collection():
    db = get_db()
    monsters_collection = db["monsters"]
    monsters_collection.insert_many(models.monsters)

def create_characters_collection():
    db = get_db()
    characters_collection = db["characters"]
    characters_collection.insert_many(models.characters)

def create_players_collection():
    db = get_db()
    characters_collection = db["players"]
    characters_collection.insert_one({"_id": 0})

def get_db():
    return DB_CLIENT[DB_NAME]

def main():
    # créer la db
    create_db()

if __name__=="__main__":
    main()
