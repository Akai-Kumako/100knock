 #72. 素性抽出

import snowballstemmer
from stop_words import get_stop_words

stemmer = snowballstemmer.stemmer("english")

BoW = {}

with open("sentiment.txt", "r") as f:
  for i in f:
    i.replace("\n", "")
    for j in i.split(" "):
      if j not in get_stop_words("english"):
        BoW[stemmer.stemWord(j)] = BoW.get(stemmer.stemWord(j), 0) + 1

for key, value in sorted(BoW.items(), key=lambda x: -x[1]):
  if value > 3:
    print(str(key) + ": " + str(value))
