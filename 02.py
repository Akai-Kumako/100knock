#02.「パトカー」＋「タクシー」＝「パタトクカシー」

a = list("パトカー")
b = list("タクシー")
i = 1

for w in b:
  a.insert(i, w)
  i += 2

a = "".join(a)

print(a)
