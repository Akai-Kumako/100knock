#35.名詞の連接

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?)$")

noun = ""
j = 0

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      if c.group(2) == "名詞":
        noun += c.group(1)
        j += 1
      else:
        if j > 1:
          print(noun) 
          j = 0
          noun = ""
