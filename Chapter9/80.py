#80. コーパスの整形

import re

stopword = re.compile("^[\.,!\?;:\(\)\[\]\'\"]|[\.,!\?;:\(\)\[\]\'\"]$")

with open("enwiki-20150112-400-r10-105752.txt", "r") as f:
  corpus = f.readlines()

with open("after-shaping-corpus-80.txt", "w") as g:
  for line in corpus:
    tokens = line.split(" ")
    for i, token in enumerate(tokens):
      tokens[i] = stopword.sub("", token)
    tokens = filter(lambda str:str != ("" or " "), tokens)
    g.write(" ".join(tokens))
