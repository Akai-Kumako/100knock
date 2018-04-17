#94. WordSimilarity-353での類似度計算

import numpy as np
import numpy.linalg as LA
import pickle
from scipy import io, sparse

com = io.loadmat("../Chapter9/WCmatrix_X")["com"]

with open("../Chapter9/t_num.pickle", "rb") as f:
  t_num = pickle.load(f)
  t_nums = t_num.keys()

with open("wordsim353/combined.tab") as f:
  combined = f.readlines()

with open("similarityfm85.txt", "w") as f:
  for data in combined:
    datas = data.split()
    try:
      mol = np.dot(com[t_num[datas[0]]], com[t_num[datas[1]]])
      den = LA.norm(com[t_num[datas[0]]]) * LA.norm(com[t_num[datas[1]]])
      if den != 0:
        cos = mol / den
      else:
        cos = -1
    except KeyError:
      cos = -1
    f.write(data.strip("\n") + "\t" + str(cos) + "\n")
