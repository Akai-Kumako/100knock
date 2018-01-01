#59. S式の解析

import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

nsubj = {}
dobj = {}

for sentence in root.iterfind("./document/sentences/sentence"):
  dependence = sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep')  
  for dep in dependence:
    if dep.get("type") == "nsubj":
      nsubj[dep.find("./governor").text] = dep.find("./dependent").text
    if dep.get("type") == "dobj":
      dobj[dep.find("./governor").text] = dep.find("./dependent").text
  for predicate in nsubj.keys():
    if predicate in dobj.keys():
      print("{}\t{}\t{}".format(nsubj[predicate], predicate, dobj[predicate]))
