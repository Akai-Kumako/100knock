#44. 係り受け木の可視化

import re
import pydot_ng as pydot

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

def graphed(edges, directed = False):
  if directed:
    graph = pydot.Dot(graph_type = "digraph")
  else:
    graph = pydot.Dot(graph_type = "graph")
  for edge in edges:
    id1 = str(edge[0][0])
    label1 = str(edge[0][1])
    id2 = str(edge[1][0])
    label2 = str(edge[1][1])
    graph.add_node(pydot.Node(id1, label=label1))
    graph.add_node(pydot.Node(id2, label=label2))
    graph.add_edge(pydot.Edge(id1, id2))
  return graph
    

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

s = neko[3]
edges = []
for i in range(len(s)):
  if s[i].string != "":
    x = s[i].dst
    if int(x) != -1:
      edges.append(((i, s[i].string), (x, s[int(x)].string)))

if len(edges) > 0:
  graph = graphed(edges, directed=True)
  graph.write_png("44.png")
