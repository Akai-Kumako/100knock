#47. 機能動詞構文のマイニング

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
    if s[i].check("動詞") and len(s[i].srcs) > 1:
      for x in s[i].srcs:
        if s[int(x)].checkSahen():
          print(s[int(x)].string + s[i].base("動詞") + "\t", end = "")
          for x in s[i].srcs[:-1]:
            if s[int(x)].check("助詞"):
              print(s[int(x)].base("助詞") + " ", end = "")
          print("\t", end ="")
          for x in s[i].srcs[:-1]:
            if s[int(x)].check("助詞"):
              print(s[int(x)].string + " ", end = "")
          print()
