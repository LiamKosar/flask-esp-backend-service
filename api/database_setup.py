import os
from pony.orm import Database, Required, db_session


def connect_to_database():
    db = Database()
    # db.bind(
    #     provider='postgres',
    #     user='defualt',
    #     password='5zsRvYe7MBtH',
    #     host='ep-calm-grass-a4wyu5pn-pooler.us-east-1.aws.neon.tech',
    #     database='verceldb',
    # )
    db.bind(provider='postgres', dsn='postgres://default:5zsRvYe7MBtH@ep-calm-grass-a4wyu5pn-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require')
    return db
