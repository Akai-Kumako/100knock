#35.名詞の連接

import re

result = re.compile("^(.*?)\t(.*?),(.*?),(.*?)$")

noun = []
j = 0

with open("neko.txt.mecab") as f:
  for i in f:
    c = result.search(i)      
    if c != None and c.group(2) == "名詞":
        noun.append(c.group(1))
    else:
      if len(noun) > 2:
        print("".join(noun))
        noun = []
