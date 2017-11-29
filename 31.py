#31.動詞

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)$")

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      if c.group(2) == "動詞":
        print(c.group(1)) 
