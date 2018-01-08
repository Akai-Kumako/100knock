#24.ファイル参照の抽出

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").split("\n")

regex = re.compile("(File|ファイル):(.*?)\|")

for j in b:
  c = regex.search(j)
  if c != None:
    print(c.group(2))
