#16.ファイルをN分割する
# split

import sys

args = sys.argv

f = open("hightemp.txt", "r")
lines = f.readlines()

n = 0

for i in range(int(args[1])):
  a = open("16out/out" + str(i) + ".txt", "w")
  for j in range((len(lines) + i) // int(args[1])):
    a.write(lines[n])
    n += 1
  a.close()

f.close()
