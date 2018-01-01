#59. S式の解析

import xml.etree.ElementTree as ET
import re

root = ET.parse("nlp.txt.xml")
phrase = re.compile("\(NP\s(.*?)\)\)")
noun = re.compile("\([A-Z]+\s(.*?)\)")

for sentence in root.iterfind("./document/sentences/sentence"):
  parse = sentence.findtext("parse")
  for n in phrase.findall(parse):
    print(re.sub("\([A-Z]+\s", "", " ".join(noun.findall(n + ")"))))
