#87. 単語の類似度

import numpy as np
import numpy.linalg as LA
import pickle
from scipy import io, sparse

com = io.loadmat("WCmatrix_X")["com"]
 
with open("t_num.pickle", "rb") as f:
  t_num = pickle.load(f)

mol = np.dot(com[t_num["United_States"]], com[t_num["U.S"]])
den = LA.norm(com[t_num["United_States"]]) * LA.norm(com[t_num["U.S"]])

print(mol / den)
