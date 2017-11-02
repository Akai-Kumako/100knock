#03.円周率

import re

a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

a = re.sub(r'[\.,]+', "", a)
a = a.split()
result = []

for w in a:
  result.append(len(w))

print(result)
