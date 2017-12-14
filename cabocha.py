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

def cabocha():
  with open("neko.txt.cabocha") as f:
    for i in f:
      if i[0] == "*" or i == "EOS\n":
        if len(chun) != 0:
          for x in rela:
            if (x[1] == idx):
              sour.append(x[0])
          chunk = Chunk(chun, dst, sour)
          sent.append(chunk)
          chun = []
          sour = []
        if i[0] == "*":
          split = re.split(" ", i)
          idx = split[1] 
          dst = split[2][:-1]
          rela.append([idx, dst])
          continue
        if i == "EOS\n" and len(sent) != 0:
          neko.append(sent)
          sent = []
          rela = []
      else:
        morp = re.split("[\t,]", i)
        morph = Morph(morp[0], morp[7], morp[1], morp[2])
        chun.append(morph)
  return neko