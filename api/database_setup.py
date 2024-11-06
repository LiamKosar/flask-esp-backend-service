import os
from pony.orm import Database

def connect_to_database():
    db = Database()
    POSTGRES_URL = os.getenv('POSTGRES_URL')
    db.bind(provider='postgres', dsn=POSTGRES_URL)
    return db
