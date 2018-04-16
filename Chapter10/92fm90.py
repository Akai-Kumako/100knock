#92. アナロジーデータへの適用 word2vec

from gensim.models import word2vec

model = word2vec.Word2Vec.load("./leaning.model")

with open("analogy-91.txt", "r") as f:
  with open("analogy-92wv.txt", "w") as g:
    analogy = f.readlines()  
    for data in analogy:
      datas = data.split()
      try:
        simi = model.wv.most_similar(positive = [datas[1], datas[2]],
                                     negative = [datas[0]],
                                     topn = 1)
      except KeyError:
        simi = [("", -1)]

      g.write(data.strip() + " " + simi[0][0] + " " + str(simi[0][1]) + "\n")
