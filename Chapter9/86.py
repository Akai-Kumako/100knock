#86. 単語ベクトルの表示

import pickle
from scipy import io, sparse

com = io.loadmat("WCmatrix_X")["com"]

with open('t_num.pickle', 'rb') as f:
  t_num = pickle.load(f)

print(com[t_num['United_States']])
