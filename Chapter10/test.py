#92. アナロジーデータへの適用 word2vec

from gensim.models import word2vec

model = word2vec.Word2Vec.load("./leaning.model")

print(model["grandpa"])
