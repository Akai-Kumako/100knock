#23.セクション構造

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").split("\n")

regex = re.compile(u"^(==+)\s*(.*?)\s*(==+)$")

for j in b:
  c = regex.search(j)
  if c != None: print("{0} [{1}]".format(c.group(2), len(c.group(1)) - 1))
