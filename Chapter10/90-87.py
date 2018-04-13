#仮初めの87

from gensim.models import word2vec
import numpy as np
import numpy.linalg as LA

model = word2vec.Word2Vec.load("./leaning.model")

mol = np.dot(model["United_States"], model["U.S"])
den = LA.norm(model["United_States"]) * LA.norm(model["U.S"])

print(mol / den)
