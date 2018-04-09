#89. 単語ベクトルの表示

import pickle
import numpy as np
import numpy.linalg as LA
from scipy import io, sparse

com = io.loadmat("WCmatrix_X")["com"]
cos = {}

with open('t_num.pickle', 'rb') as f:
  t_num = pickle.load(f)

Greece = com[t_num["Spain"]] - com[t_num["Madrid"]] + com[t_num["Athens"]]

for t in t_num.keys():
  mol = np.dot(Greece, com[t_num[t]])
  den = LA.norm(Greece) * LA.norm(com[t_num[t]])
  if den != 0:
    cos[t] = mol / den
  else:
    cos[t] = -1

for key, value in sorted(cos.items(), key=lambda x: -x[1])[:10]:
  print(key + "\t" + str(value))
