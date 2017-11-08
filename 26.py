#26.強調マークアップの除去

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").split("\n")

info = {}

for j in b:
  c = re.search(u"^\|(.*?)\s*=\s*(.*?)$", j)
  if c != None: info[c.group(1)] = re.sub("'{2, 5}", "", c.group(2))
  if j == "}}": break

for k, v in info.items():
  print("{0}: {1}".format(k, v))
