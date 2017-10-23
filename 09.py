#09.Typoglycemia

import random

a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

a = a.split(" ")
chimera = []

for word in a:
  if 4 < len(word):
    chars = list(word[1:-1])
    random.shuffle(chars)
    chimera.append(word[0] + "".join(chars) + word[-1])
  else:
    chimera.append(word)

print(" ".join(chimera))
