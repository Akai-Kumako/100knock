#54. 品詞タグ付け
import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

for token in root.iter("token"):
  print('{}\t{}\t{}'.format(token.findtext('word'), 
                            token.findtext('lemma'), 
                            token.findtext('POS')))
