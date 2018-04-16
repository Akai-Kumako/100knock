#93. アナロジータスクの正解率の計算

with open("analogy-92pp.txt", "r") as f:
  analogy = f.readlines()
  n = len(analogy)
  a = 0
  for data in analogy:
    items = data.split()
    if items[4] in items[3]:
      a += 1

print(a / n)

with open("analogy-92wv.txt", "r") as f:
  analogy = f.readlines()
  n = len(analogy)
  a = 0
  for data in analogy:
    items = data.split()
    if items[4] in items[3]:
      a += 1

print(a / n)
