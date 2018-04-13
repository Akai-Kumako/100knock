#90. word2vecによる学習

from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('../Chapter9/after-shaping-corpus-81.txt')

model = word2vec.Word2Vec(sentences, size=300, min_count=10, window=15)
model.save("./leaning.model")
