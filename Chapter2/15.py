#15.末尾のN行を出力
# tail -n N hightemp.txt

import sys

args = sys.argv

f = open("hightemp.txt", "r")
lines = f.readlines()

for i in range(len(lines) - int(args[1]), len(lines)):
  print(lines[i], end = "")

f.close()
