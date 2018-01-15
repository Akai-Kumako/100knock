#65. MongoDBの検索

#insert_one 10:25 69
#insert_manyの方が早いらしい

import json
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.kyoko
co = db.nlp_collection

for data in co.find({"name": "Queen"}):
  print(data)
