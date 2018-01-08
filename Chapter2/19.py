#19.各行の1コラム目の文字列の出現頻度を求め、出現頻度を高い順に並べる
# cut -f1 hightemp.txt | sort | uniq -c | sort --reverse

import sys

args = sys.argv

f = open("hightemp.txt", "r")
lines = f.readlines()

a = {}

for i in range(len(lines)):
  line = lines[i].split("\t")
  a[line[0]] = a.get(line[0], 0) + 1

b = sorted(a.items(), key=lambda x: x[1])

for i in reversed(b):
  print(i)

f.close()
