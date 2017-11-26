#26.強調マークアップの除去

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").replace("<br/>\n").split("\n")

info = {}
regex = re.compile(u"^\|(.*?)\s*=\s*(.*?)$")
emph = re.compile("'{2,5}")

for j in b:
  c = regex.search(j)
  if c != None: info[c.group(1)] = emph.sub("", c.group(2))
  if j == "}}": break

for k, v in info.items():
  print("{0}: {1}".format(k, v))
