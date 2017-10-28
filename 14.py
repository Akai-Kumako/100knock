#14.先頭からN行を出力
# head -n N hightemp.txt

import sys

args = sys.argv

f = open("hightemp.txt", "r")
lines = f.readlines()

for i in range(int(args[1])):
  print(lines[i], end = "")

f.close()
