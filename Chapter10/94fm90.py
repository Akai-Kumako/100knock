#94. WordSimilarity-353での類似度計算

from gensim.models import word2vec
import numpy as np
import numpy.linalg as LA

model = word2vec.Word2Vec.load("./leaning.model")

with open("wordsim353/combined.tab") as f:
  combined = f.readlines()

with open("similarityfm90.txt", "w") as f:
  for data in combined:
    datas = data.split()
    try:
      mol = np.dot(model[datas[0]], model[datas[1]])
      den = LA.norm(model[datas[0]]) * LA.norm(model[datas[1]])
      if den != 0:
        cos = mol / den
      else:
        cos = -1
    except KeyError:
      cos = -1
    f.write(data.strip("\n") + "\t" + str(cos) + "\n")
