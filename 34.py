#34.「AのB」

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?)$")

sent = [{"dummy" : ""}, {"dummy": ""}]

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      prov = {
        "surface" : c.group(1),
        "pos" : c.group(2),
        "pos2" : c.group(3)
      }
    sent.append(prov)
    A = sent[-3]
    no = sent[-2]
    B = sent[-1]
    if A.get("pos") == "名詞" and no.get("pos2") == "連体化" and B.get("pos") == "名詞":
       print("".join([  A.get("surface"),
                        no.get("surface"),
                        B.get("surface")
       ]))
