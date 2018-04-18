#84. 単語文脈行列の作成

import re
import math
import pickle
from scipy import io, sparse

rejex = re.compile("(.*?)\t(.*?)\n")
co_rejex = re.compile("(.*?)\t(.*?)\t(.*?)\n")

ts = {}
t_num = {}
cs = {}
c_num = {}

with open("freq-t.txt", "r") as f:
  t_occ = f.readlines()
  for i, s in enumerate(t_occ):
    a = rejex.search(s)
    ts[a.group(1)] = int(a.group(2))  
    t_num[a.group(1)] = i    

with open("freq-c.txt", "r") as f:
  c_occ = f.readlines()
  for i, s in enumerate(c_occ):
    a = rejex.search(s)
    cs[a.group(1)] = int(a.group(2))  
    c_num[a.group(1)] = i    

det = sparse.lil_matrix((len(ts), len(cs)))

with open("freq-co.txt", "r") as f:
  co_occ = f.readlines()
  for s in co_occ:
    a = co_rejex.search(s)
    if int(a.group(3)) > 9:
      t = ts[a.group(1)]
      c = cs[a.group(2)]
      ppmi = max([math.log((69289061 * int(a.group(3))) / (t * c)), 0])
      det[t_num[a.group(1)], c_num[a.group(2)]] = ppmi

with open("t_num.pickle", "wb") as f:
  pickle.dump(t_num, f)
with open("c_num.pickle", "wb") as f:
  pickle.dump(c_num, f)
io.savemat("WCmatrix", {"det":det})
