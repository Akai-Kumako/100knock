#50. 文区切り

import re

punc = re.compile(r"(.*?[\.;:\?!]) ([A-Z])")

nlp = []

with open("nlp.txt") as f:
  for s in f.readlines():
    if s == "\n":
      continue
    nlp.extend(punc.sub(r"\1\n\2", s).split("\n"))

while nlp.count(""):
  nlp.remove("")

for s in nlp:
  print(s)
