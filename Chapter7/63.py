#63. オブジェクトを値に格納したKVS

import plyvel
import pickle
import json

artists = plyvel.DB('/tmp/kyoko2.ldb', create_if_missing=True)

#with open("artist.json", "r") as f:
#  for i in f:
#    a = json.loads(i)
#    d = artists.get(a.get("name", "").encode("utf-8"))
#    if d == None:
#      dic = {}
#      dic[0] = a.get("tags")
#    else:
#      dic = pickle.loads(d)
#      dic[len(dic)] = a.get("tags")
#    artists.put(a.get("name", "").encode('utf-8'), pickle.dumps(dic))

artist = pickle.loads(artists.get("Oasis".encode("utf-8")))

for key, value in artist.items():
  print("No.{}".format(key + 1))
  if value == None:
    print("\tNo tag")
    continue
  for tag in value:
    print("\t{}\t{}".format(tag.get("value"), tag.get("count")))
