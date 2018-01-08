#05.n-gram

a = "I am an NLPer"

word = a.split()
char = list(a)

def ngram(target, n):
  result = []
  if len(target) >= n:
    for i in range(len(target) - n + 1):
      result.append("".join(target[i:i + n]))
  return result  

print(ngram(word, 2))
print(ngram(char, 2))
