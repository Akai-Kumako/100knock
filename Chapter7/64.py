#64. MongoDBの構築

#insert_one 10:25 69
#insert_manyの方が早いらしい

import json
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
client = MongoClient('localhost', 27017)

db = client.kyoko
co = db.nlp_collection

with open("artist.json", "r") as f:
  for i in f:
    a = json.loads(i)
    co.insert_one(a)

co.create_index([("name", ASCENDING)])
co.create_index([("aliases.name", ASCENDING)])
co.create_index([("tags.value", ASCENDING)])
co.create_index([("rating.value", ASCENDING)])
