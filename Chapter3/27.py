#27.内部リンクの除去

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").replace("<br/>\n", "").split("\n")

info = {}
regex = re.compile(u"^\|(.*?)\s*=\s*(.*?)$")
emph = re.compile("'{2,5}")
link = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")

for j in b:
  c = regex.search(j)
  if c != None:
    d = link.search(j)
    if d != None:
      info[c.group(1)] = d.group(3)
    else: info[c.group(1)] = emph.sub("", c.group(2))
  if j == "}}": break

for k, v in info.items():
  print("{0}: {1}".format(k, v))
