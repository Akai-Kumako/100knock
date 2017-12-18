#43. 名詞を含む文節が動詞を含む文節に係るものを抽出

import re

neko = []
sent = []
chun = []
morp = []

rela = []
sour = []

class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

class Chunk:
  def __init__(self, morphs, dst, srcs):
    self.morphs = morphs
    self.dst = dst
    self.srcs = srcs
    self.string = ""
    for s in self.morphs:
      self.string += s.surface

  def check(self, pos):
    for morph in self.morphs:
      if morph.pos == pos:
        return True
    return False

  def base(self, pos):
    for morph in self.morphs:
      if morph.pos == pos:
        return morph.base
    return None
  
  def checkSahen(self):
    if self.morphs[0].pos1 == "サ変接続" and len(self.morphs) > 1:
      if self.morphs[1].pos == "助詞" and self.morphs[1].surface == "を":
        return True
    return False

with open("neko.txt.cabocha") as f:
  for i in f:
    if i[0] == "*":
      split = re.split(" ", i)
      if len(chun) != 0:
        for x in rela:
          if (x[1] == idx):
            sour.append(x[0])
        chunk = Chunk(chun, dst, sour)
        sent.append(chunk)
        chun = []
        sour = []
      idx = split[1] 
      dst = split[2][:-1]
      rela.append([idx, dst])
      continue
    if i == "EOS\n":
      if len(chun) != 0:
        for x in rela:
          if (x[1] == idx):
            sour.append(x[0])
        chunk = Chunk(chun, dst, sour)
        sent.append(chunk)
        chun = []
        sour = []
      if len(sent) != 0:
        neko.append(sent)
        sent = []
        rela = []
    else:
      morp = re.split("[\t,]", i)
      if morp[1] != "記号":
        morph = Morph(morp[0], morp[7], morp[1], morp[2])
      else:
        morph = Morph("", "", "", "")
      chun.append(morph)

for s in neko:
  for i in range(len(s)):
    if s[i].check("名詞") and s[i].dst != -1:
      if int(s[i].dst) == -1:
        continue
      print(s[i].string, end = "")
      dst = int(s[i].dst)
      while dst != -1:
        print(" -> " + s[dst].string, end = "")
        dst = int(s[dst].dst)
      print()
