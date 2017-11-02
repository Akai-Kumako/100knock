#18.各行を3コラム目の数値の降順にソート
# cat hightemp.txt | awk '{print $1}' | sort | uniq

import sys

args = sys.argv

f = open("hightemp.txt", "r")
lines = f.readlines()

a = {}

for i in range(len(lines)):
  line = lines[i].split("\t")
  a[lines[i]] = line[2]

b = sorted(a.items(), key=lambda x: x[1])

for i in reversed(b):
  print(i[0], end = "")

f.close()
