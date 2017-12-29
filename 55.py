#55. 固有表現抽出
import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

for token in root.iter("token"):
  if token.findtext("NER") == "PERSON":
    print(token.findtext("word"))
