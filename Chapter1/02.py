#02.「パトカー」＋「タクシー」＝「パタトクカシー」

a = list("パトカー")
b = list("タクシー")
c = []

for i, j in zip(a, b):
  c += i + j

c = "".join(c)

print(c)
