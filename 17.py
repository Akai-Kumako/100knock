#17.1列目の文字列の異なり
# cat hightemp.txt | awk '{print $1}' | sort | uniq

import sys

args = sys.argv

f = open("hightemp.txt", "r")
lines = f.readlines()

a = set([])

for i in range(len(lines)):
  line = lines[i].split("\t")
  a.add(line[0])

print(a)

f.close()
