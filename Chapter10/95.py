#95. WordSimilariy-353での類似度計算

import numpy as np
import math

with open("similarityfm85.txt", "r") as f:
  fm85 = f.readlines()
  hum = []
  com = []
  diffs = 1
  for data in fm85[1:]:
    datas = data.split()
    hum.append(float(datas[2]))
    com.append(float(datas[3]))
  for i, v in enumerate(np.argsort(hum)):
    diffs += pow((i + 1) - (list(np.argsort(com)).index(v) + 1), 2)
  spear = 1.0 - ((6.0 * diffs) / (pow(len(com), 3) - len(com)))
  print("fm85: " + str(spear))

with open("similarityfm90.txt", "r") as f:
  fm90 = f.readlines()
  hum = []
  com = []
  diffs = 1
  for data in fm90[1:]:
    datas = data.split()
    hum.append(float(datas[2]))
    com.append(float(datas[3]))
  for i, v in enumerate(np.argsort(hum)):
    diffs += pow((i + 1) - (list(np.argsort(com)).index(v) + 1), 2)
  spear = 1.0 - ((6.0 * diffs) / (pow(len(com), 3) - len(com)))
  print("fm90: " + str(spear))
