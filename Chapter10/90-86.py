#仮初めの86 

from gensim.models import word2vec

model = word2vec.Word2Vec.load("./leaning.model")
print(model["United_States"])
