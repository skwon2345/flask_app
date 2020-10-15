from flask_pymongo import PyMongo
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

db_url = os.environ.get("DB_URL")

client = MongoClient(db_url)

db = client.test_db