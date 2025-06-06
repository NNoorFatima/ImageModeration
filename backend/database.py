import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["image_moderation"]  #db name

tokens_collection = db.tokens
usages_collection = db.usages
