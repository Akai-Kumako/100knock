#96. 国名に関するベクトルの抽出

from gensim.models import word2vec
import pickle

model = word2vec.Word2Vec.load("./leaning.model")

with open("../Chapter9/nations.txt", "r") as f:
  nations = f.readlines()

vecs = {}
names = []

for nation in nations:
  name = nation.strip("\n").replace(" ", "_")
  try:
    vecs[name] = model[nation.strip("\n").replace(" ", "_")]
    names.append(name)
  except KeyError:
    pass

with open("nations_vec.pickle", "wb") as f:
  pickle.dump(vecs, f)

with open("nations_name.pickle", "wb") as f:
  pickle.dump(names, f)
