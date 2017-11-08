#22.カテゴリ名の抽出

import json
import re

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").split("\n")

for j in b:
  if "Category" in j:
    print(re.search("^\[\[Category:(.*?)(\|.*)*\]\]$", j).group(1))
