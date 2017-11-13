#28.MediaWikiマークアップの除去

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").split("\n")

info = {}
regex = re.compile(u"^\|(.*?)\s*=\s*(.*?)$")
emph = re.compile("'{2,5}")
intl = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
tag = re.compile(r"<\/?[ref|br][^>]*?>")
extl = re.compile(r"\[http:\/\/[^\]]*?\]")

def remove(text):
  text = emph.sub("", text)
  prov = intl.search(text)
  if prov != None:
    text = prov.group(3)
  text = tag.sub("", text)
  text = extl.sub("", text)
  
  return text

for j in b:
  c = regex.search(j)
  if c != None:
    info[c.group(1)] = remove(c.group(2))
  if j == "}}": break

for k, v in info.items():
  print("{0}: {1}".format(k, v))
