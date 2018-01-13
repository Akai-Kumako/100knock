#60. KVSの構築

import plyvel
import json
import pickle

artists = plyvel.DB('/tmp/artist.ldb', create_if_missing=True)

with open("artist.json", "r") as f:
  for i in f:
    a = json.loads(i)
    artists.put(a.get("name").encode("utf-8"),
                a.get("area", "").encode("utf-8"))
