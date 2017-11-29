#38.ヒストグラム

import numpy as np
import pylab as plt
import re
import matplotlib as mpl

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

mpl.rcParams['font.family'] = "AppleGothic"
plt.hist(x, bins = 50, range = (1, 50))

plt.show() 
