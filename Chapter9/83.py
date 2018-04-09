#83. 単語/文脈の頻度の計測

with open("contexts.txt", "r") as f:
  contexts = f.readlines()

co = {}
t = {}
c = {}

for context in contexts:
  pair = context.split()
  if len(pair) == 2:
    co[context] = co.get(context, 0) + 1
    t[pair[0]] = t.get(pair[0], 0) + 1
    c[pair[1]] = c.get(pair[1], 0) + 1

with open("freq-co.txt", "w") as f:
  for key, value in co.items():
    f.write(key.replace("\n", "") + "\t" + str(value) + "\n")

with open("freq-t.txt", "w") as f:
  for key, value in t.items():
    f.write(key + "\t" + str(value) + "\n")

with open("freq-c.txt", "w") as f:
  for key, value in c.items():
    f.write(key + "\t" + str(value) + "\n")

print(len(contexts))
