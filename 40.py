#40. 係り受け解析結果の読み込み（形態素）

import re

neko = []
sent = []
morp = []

class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

with open("neko.txt.cabocha") as f:
  for i in f:
    if i[0] == "*":
      continue
    if i == "EOS\n":
      if len(sent) != 0:
        neko.append(sent)
        sent = []
    else:
      morp = re.split("[\t,]", i)
      morph = Morph(morp[0], morp[7], morp[1], morp[2])
      sent.append(morph)

for s in neko[2]:
  print("surface: {}, base: {}, pos: {}, pos1: {}".format(s.surface, s.base, s.pos, s.pos1))
