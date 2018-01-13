#68. ソート

import json
from pymongo import MongoClient
from pymongo import DESCENDING
client = MongoClient('localhost', 27017)

db = client.nlp_database
co = db.nlp_collection

data = co.find({"tags.value": "dance"})
sort = data.sort("rating.count", DESCENDING)

for index, value in enumerate(sort, start = 1):
  print("{}\t{}".format(index, value.get("name")))
  if index == 10:
    break
