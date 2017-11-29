#36.単語の出現頻度

import re

result = re.compile("^(.*?)\t(.*?)$")

neko = {}

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      neko[c.group(1)] = neko.get(c.group(1), 0) + 1

print(sorted(neko.items(), key = lambda x: -x[1]))
