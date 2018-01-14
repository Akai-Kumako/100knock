#60. KVSの構築

import plyvel
import json
import pickle

artists = plyvel.DB('/tmp/kyoko.ldb', create_if_missing=True)

with open("artist.json", "r") as f:
  for i in f:
    a = json.loads(i)
    area = artists.get(a.get("name").encode("utf-8"))
    if area == None or area == "":
      artists.put(a.get("name").encode("utf-8"),
                  a.get("area", "").encode("utf-8"))
    else:
      artists.put(a.get("name").encode("utf-8"),
                 (area.decode("utf-8") + "\n" + a.get("area", "")).encode("utf-8"))

artists.close()
