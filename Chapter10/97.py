#97. k-meansクラスタリング

import pickle
import numpy as np
import numpy.linalg as LA
from numpy.random import *

with open("nations_vec.pickle", "rb") as f:
  vecs = pickle.load(f)

with open("nations_name.pickle", "rb") as f:
  names = pickle.load(f)

groups = []
n = 0

for i in range(5):
  a = []
  for j in range((len(names) + 1) // 5):
    a.append(names[n])
    n += 1
  groups.append(a)

centroid = []

for i in range(5):
  centroid.append(np.average([vecs[j] for j in groups[i]], axis = 0))

clus = False

nearests = [[], [], [], [], []]
old_nearests = [[], [], [], [], []]

while clus == False:
  nearests = [[], [], [], [], []]
  print("KYOKO")
  for name in names:
    cos = []
    for i in range(5):
      mol = np.dot(vecs[name], centroid[i])
      den = LA.norm(vecs[name]) * LA.norm(centroid[i])
      if den != 0:
        cos.append(mol / den)
    nearests[np.argsort(cos)[0]].append(vecs[name])
  print(nearests)
  if nearests == old_nearests:
    clus = True
  else:
    for i in range(5):
      centroid = []
      centroid.append(np.average(nearests[i], axis = 0))
    old_nearests = nearests

print("KYOKO")

for i in range(5):
  for j in nearests[i]:
    print(i + " :\n" + [k for k, v in vecs.items() if v == j])
