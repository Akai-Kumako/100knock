 #73. 素性抽出

import snowballstemmer
stemmer = snowballstemmer.stemmer("english")

stopword = [".", ",", "the", "a", "and", "of", "it", "to", "is",
            "that", "in", "\"", "with", "as", "but", "an", "for",
            "this", "be", "you", "on", "one", "by", "has", "not",
            "at", "about", "from", "his", "are", "", "--"]

PBoW = {}
NBoW = {}
PAoW = 0
NAoW = 0

with open("rt-polarity.pos", "r", encoding = "ISO-8859-1") as f:
  for i in f:
    i.replace("\n", "")
    for j in i.split(" "):
      if j not in stopword:
        PBoW[stemmer.stemWord(j)] = PBoW.get(stemmer.stemWord(j), 0) + 1
        PAoW += 1

with open("rt-polarity.neg", "r", encoding = "ISO-8859-1") as g:
  for i in g:
    i.replace("\n", "")
    for j in i.split(" "):
      if j not in stopword:
        NBoW[stemmer.stemWord(j)] = NBoW.get(stemmer.stemWord(j), 0) + 1
        NAoW += 1

sample_word = "inform"

print(PBoW.get(sample_word, 0))
print(NBoW.get(sample_word, 0))

#def logistic(word):
#  if PBoW.count(word)
