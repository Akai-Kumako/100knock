#59. S式の解析

import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

for sentence in root.iterfind("./document/sentences/sentence"):
  parse = sentence.findtext("parse")
  ss = parse.split(" ")
  now = 0
  for s in ss:
    if s == "":
      continue    
    elif s[0] == "(":
      if s == "(NP":
        lsb = 0
        rsb = 0
        for w in ss[now + 1:]:
          if w == "" or lsb - rsb < 0:
            continue
          elif w[0] == "(":
            lsb += 1
          elif w[-1] == ")":
            rsb += w.count(")")
            print(w[:len(w)-w.count(")")], end = " ")
        print()
    now += 1
