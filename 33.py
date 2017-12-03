#33.サ変名詞

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?)$")

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None:
      if c.group(2) == "名詞" and c.group(3) == "サ変接続":
        print(c.group(1)) 
