#63. オブジェクトを値に格納したKVS

import plyvel
import pickle
#import json

artists = plyvel.DB('/tmp/nlp2.ldb', create_if_missing=True)

#with open("artist.json", "r") as f:
#  for i in f:
#    a = json.loads(i)
#    tags = pickle.dumps(a.get("tags"))
#    artists.put(a.get("name", "").encode('utf-8'), tags)

artist = pickle.loads(artists.get("Oasis".encode("utf-8")))

for tag in artist:
  print("{}\t{}".format(tag.get("value"), tag.get("count")))
