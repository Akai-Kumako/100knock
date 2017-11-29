#39.Zipfの法則

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

x = {}

for k, v in sorted(neko.items(), key = lambda x: -x[1]): 
  x[v] = x.get(v, 0) + 1

left = list(x.keys())
height = sorted(list(x.values()))

plt.plot(left, height);

plt.xscale('log')
plt.yscale('log')
plt.xlabel("Occurrence frequency rank")
plt.ylabel("Frequency of appearance")

plt.show() 
