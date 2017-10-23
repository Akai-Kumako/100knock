#06.集合

a = "paraparaparadise"
b = "paragraph"

charA = list(a)
charB = list(b)

def ngram(target, n):
  result = []
  if len(target) >= n:
    for i in range(len(target) - n + 1):
      result.append("".join(target[i:i + n]))
  return result  

setA = set(ngram(charA, 2))
setB = set(ngram(charB, 2))

print(setA | setB)
print(setA & setB)
print(setA.difference(setB))
print(setB.difference(setA))

print("se" in setA)
print("se" in setB)
