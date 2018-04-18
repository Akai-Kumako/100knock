#仮初めの89

from gensim.models import word2vec

model = word2vec.Word2Vec.load("./leaning.model")

with open("analogy-91.txt") as f:
  analogy = f.readline()

coss = model.wv.most_similar(positive = ["Spain", "Athens"], negative = ["Madrid"])

for cos in coss:
  print(cos)
