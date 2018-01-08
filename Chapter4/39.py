#39.Zipfの法則

import numpy as np
import matplotlib.pyplot as plt
import re

result = re.compile("^(.*?)\t(.*?)$")

neko = {}

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      neko[c.group(1)] = neko.get(c.group(1), 0) + 1

x = []

for k, v in sorted(neko.items(), key = lambda x: x[1]): 
  x.append(v)

plt.xscale('log')
plt.yscale('log')
plt.plot(x)

plt.xlabel("Occurrence frequency rank")
plt.ylabel("Frequency of appearance")

plt.show() 
