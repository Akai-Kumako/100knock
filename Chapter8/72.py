 #72. 素性抽出

import snowballstemmer
stemmer = snowballstemmer.stemmer("english")

stopword = [".", ",", "the", "a", "and", "of", "it", "to", "is",
            "that", "in", "\r", "with", "as", "but", "an", "for",
            "this", "be", "you", "on", "one", "by", "has", "not",
            "at", "about", "from", "his", "are", "", "--"]

BoW = {}

with open("rt-polarity.pos", "r", encoding = "ISO-8859-1") as f:
  for i in f:
    i.replace("\n", "")
    for j in i.split(" "):
      if j not in stopword:
        BoW[stemmer.stemWord(j)] = BoW.get(stemmer.stemWord(j), 0) + 1

for key, value in sorted(BoW.items(), key=lambda x: -x[1]):
    print(str(key) + ": " + str(value))
