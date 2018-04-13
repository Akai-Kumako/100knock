#仮初めの88

from gensim.models import word2vec
import numpy as np
import numpy.linalg as LA

model = word2vec.Word2Vec.load("./leaning.model")

coss = model.wv.most_similar(["United_States"], [], 10)

for cos in coss:
  print(cos)
