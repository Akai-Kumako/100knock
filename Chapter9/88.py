#88. 類似度の高い単語10件

import pickle
import numpy as np
import numpy.linalg as LA
from scipy import io, sparse

com = io.loadmat("WCmatrix_X")["com"]
cos = {}

with open('t_num.pickle', 'rb') as f:
  t_num = pickle.load(f)

for t in t_num.keys():
  if t == "England":
    continue
  mol = np.dot(com[t_num["England"]], com[t_num[t]])
  den = LA.norm(com[t_num["England"]]) * LA.norm(com[t_num[t]])
  if den != 0:
    cos[t] = mol / den
  else:
    cos[t] = -1

for key, value in sorted(cos.items(), key=lambda x: -x[1])[:10]:
  print(key + "\t" + str(value))
