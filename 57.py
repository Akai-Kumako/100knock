#57. 係り受け解析

import xml.etree.ElementTree as ET
import pydot_ng as pydot

root = ET.parse("nlp.txt.xml")

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

for sentence in root.iterfind("./document/sentences/sentence"):
  s = int(sentence.get("id"))
  edges = []
  dependence = sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep')  
  for dep in dependence:
    if dep.get("type") != "punct" and dep.get("type") != "root":
      edges.append(((dep.find("./governor").get("idx"), dep.find("./governor").text),
                    (dep.find("./dependent").get("idx"), dep.find("./dependent").text)))
  if len(edges) > 0:
    graph = graphed(edges, directed=True)
    graph.write_png("output/57out/{}.png".format(s))
