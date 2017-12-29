#53. Tokenization
import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

for word in root.iter("word"):
    print(word.text)
