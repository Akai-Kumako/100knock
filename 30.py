#30.形態素解析結果の読み込み

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)$")

neko = []
sent = []

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      prov = {
        "surface" : c.group(1),
        "base" : c.group(8),
        "pos" : c.group(2),
        "pos2" : c.group(3)
      }
      sent.append(prov)
      if c.group(3) == "句点":
        neko.append(sent)
        sent = []

for sent in neko:
  for word in sent:
    print(word["surface"], word["base"], word["pos"], word["pos2"])
