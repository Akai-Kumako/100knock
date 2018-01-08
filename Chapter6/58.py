#58. タプルの抽出

import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

for sentence in root.iterfind("./document/sentences/sentence"):
  dependence = sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep')  
  nsubj = {}
  dobj = {}
  pred = {}
  for dep in dependence:
    gove = dep.find("./governor").text
    depe = dep.find("./dependent").text
    idx = dep.find("./governor").get("idx")
    pred[idx] = gove
    if dep.get("type") == "nsubj":
      nsubj[idx] = depe
    if dep.get("type") == "dobj":
      dobj[idx] = depe
  for idx in nsubj.keys():
    if idx in dobj.keys() and idx in nsubj.keys():
      print("{}\t{}\t{}".format(nsubj[idx], pred[idx], dobj[idx]))
