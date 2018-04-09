#82. 文脈の抽出

import random

with open("after-shaping-corpus-81.txt", "r") as f:
  corpus = f.readlines()

with open("contexts.txt", "w") as g:
  for line in corpus:
    line = line.replace("\n", "")
    tokens = line.split(" ")
    for i, token in enumerate(tokens):
      num = random.randint(1, 5)
      context = tokens[max([i-num, 0]) : min([i+num+1, len(tokens)])]
      for c in context:
        if c != token and token != "" and c != "":
          g.write(token + "\t" + c + "\n")
