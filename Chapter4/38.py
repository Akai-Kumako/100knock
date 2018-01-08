#38.ヒストグラム

import numpy as np
import pylab as plt
import re

result = re.compile("^(.*?)\t(.*?)$")

neko = {}

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      neko[c.group(1)] = neko.get(c.group(1), 0) + 1

x = []

for k, v in sorted(neko.items(), key = lambda x: -x[1]): 
  x.append(v)

plt.hist(x, bins = 30, range = (1, 30))

plt.xlabel("Frequency of appearance")
plt.ylabel("Number of word types")

plt.show() 
