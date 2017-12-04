#30.形態素解析結果の読み込み

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)$")

neko = []
sent = []

with open("neko.txt.mecab") as f:
  for i in f:
    if i == "EOS\n":
      neko.append(sent)
      sent = []
    c = result.search(i)      
    if c != None:
      prov = {
        "surface" : c.group(1),
        "base" : c.group(8).split(",", 1)[0],
        "pos" : c.group(2),
        "pos2" : c.group(3) 
      }
      sent.append(prov)

for sent in neko:
  for word in sent:
    print(word["surface"], word["base"], word["pos"], word["pos2"])
  print()
