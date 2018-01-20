#70. データの入手・整形

import random

pos = 0
neg = 0

def shaping(name, opt):
  with open(name, "r+", encoding = "ISO-8859-1") as f:
    assu = ""
    for i in f:
      assu += (opt + " " + i)
    f.seek(0)
    try: f.write(assu)
    except IOError: pass
 
#shaping("rt-polarity.pos", "1")
#shaping("rt-polarity.neg", "0")

with open("sentiment.txt", "w") as g:
  sent = []
  with open("rt-polarity.pos", "r", encoding = "ISO-8859-1") as a:
    sent.extend(a.readlines())
  with open("rt-polarity.neg", "r", encoding = "ISO-8859-1") as b:
    sent.extend(b.readlines())
  random.shuffle(sent)
  g.write("".join(sent))

with open("sentiment.txt", "r") as g:
  for i in g:
    if "+1" in i:
      pos += 1
    elif "-1" in i:
      neg += 1

print("pos : {}".format(pos))
print("neg : {}".format(neg))
