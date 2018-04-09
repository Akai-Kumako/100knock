#81. 複合語からなる国名への対処

with open("after-shaping-corpus-80.txt", "r") as f:
  corpus = f.read()

with open("nations.txt", "r") as g:
  nations = g.readlines()

with open("after-shaping-corpus-81.txt", "w") as h:
  for nation in nations:
    nation = nation.replace("\n", "")
    corpus = corpus.replace(nation, nation.replace(" ", "_"))
  h.write(corpus)
