#97. k-meansクラスタリング

import pickle

with open("nations_vec.pickle", "rb") as f:
  vecs = pickle.load(f)

with open("nations_name.pickle", "rb") as f:
  names = pickle.load(f)

length = len(names)

print(names)

print(length)
