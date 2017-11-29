#37.頻度上位10語

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

left = range(1, 11)
height = []
label = []

for k, v in sorted(neko.items(), key = lambda x: -x[1])[0:10]: 
  height.append(v)
  label.append(k)

mpl.rcParams['font.family'] = "AppleGothic"
plt.bar(left, height, tick_label=label, align="center")

plt.show() 
