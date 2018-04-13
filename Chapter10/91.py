#91. アナロジーデータの準備

import re

analogy = re.compile(": family\n([\s\S]*?)\n:")

with open("analogy.txt", "r") as f:
  data = f.read()
  a = analogy.search(data)
  with open("analogy-91.txt", "w") as g:
    g.write(a.group(1))
