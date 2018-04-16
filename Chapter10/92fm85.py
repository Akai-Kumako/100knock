#92. アナロジーデータへの適用 ppmi

import pickle
import numpy as np
import numpy.linalg as LA
from scipy import io, sparse

com = io.loadmat("../Chapter9/WCmatrix_X")["com"]
cos = {}

with open("../Chapter9/t_num.pickle", "rb") as f:
  t_num = pickle.load(f)

with open("analogy-91.txt", "r") as f:
  with open("analogy-92pp.txt", "w") as g:
    analogy = f.readlines()  
    for data in analogy:
      datas = data.split()
      ts = t_num.keys()
      if datas[0] in ts and datas[1] in ts and datas[2] in ts: 
        simi = com[t_num[datas[1]]] - com[t_num[datas[0]]] + com[t_num[datas[2]]]
        for t in t_num.keys():
          mol = np.dot(simi, com[t_num[t]])
          den = LA.norm(simi) * LA.norm(com[t_num[t]])         
          if den != 0:
            cos[t] = mol / den
          else:
            cos[t] = -1 
        for key, value in sorted(cos.items(), key=lambda x: -x[1])[:1]:
          g.write(data.strip() + " " + key + " " + str(value) + "\n")
      else:
        g.write(data.strip() + "  -1" + "\n")
