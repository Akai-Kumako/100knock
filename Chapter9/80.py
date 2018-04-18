#80. コーパスの整形

import re

with open("enwiki-20150112-400-r100-10576.txt", "r") as f:
  corpus = f.readlines()

with open("after-shaping-corpus-80.txt", "w") as g:
  for line in corpus:
    tokens = line.split(" ")
    for i, token in enumerate(tokens):
      tokens[i] = token.strip().strip('.,!?;:()[]\'"')
    g.write(" ".join(tokens))
