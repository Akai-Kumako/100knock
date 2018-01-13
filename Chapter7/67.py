#67. 複数のドキュメントの取得

import json
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.nlp_database
co = db.nlp_collection

for data in co.find({"aliases.name": "オアシス"}):
  print(data)
