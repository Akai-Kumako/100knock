#21.カテゴリ名を含む行を抽出

import json

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").split("\n")

for i in b:
  if "Category" in i:
    print(i)
