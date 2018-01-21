 #75. 素性の重み

import snowballstemmer
import math
from stop_words import get_stop_words
from collections import defaultdict

stemmer = snowballstemmer.stemmer("english")

N = 10
eta0 = 0.1

def train(data):
    t = 1
    W = defaultdict(float)
    for i in range(N):
        for line in data:
            update(W, line[1:], float(line[0]), eta0 / (1 + t / float(len(data))))
            t += 1
    return W

def update(W, X, l, eta):
    a = sum([W[x] for x in X])
    g = ((1. / (1. + math.exp(-a))) - l) if -100. < a else (0. - l)
    for x in X:
        W[x] -= eta * g

with open("sentiment.txt") as f:
  data = []
  for i in f:
    a = i.replace("+1", "1").replace("-1", "0").strip("\n").split()
    sent = []
    for j in a:
      j = stemmer.stemWord(j)
      if j not in get_stop_words("english"):
        sent.append(j)
    data.append(sent)

a = train(data)

for k, v in sorted(a.items(), key=lambda x: -x[1])[:10]:
  print("{}\t{}".format(k, v))

for k, v in sorted(a.items(), key=lambda x: x[1])[:10]:
  print("{}\t{}".format(k, v))
