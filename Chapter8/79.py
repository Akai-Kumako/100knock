 #79. 適合率-再現率グラフの描画

import snowballstemmer
import math
from stop_words import get_stop_words
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

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

def predict(dic, word_list):
    cnt = 0.
    for word in word_list:
        word = (word)
        if word in dic:
            cnt += dic[word]
    rate = (1. / (1. + math.exp(-cnt)))
    return rate

with open("sentiment.txt") as f:
  lines = f.readlines()
  
line = []
n = 0
for i in range(5):
  a = []
  for j in range((len(lines) + i) // 5):
    a.append(lines[n])
    n += 1
  line.append(a)  

precisions = []
recalls = []

for thr in np.arange(0.02,1.0,0.05):
  precision = []
  recall = []
  for z in range(5):
    data = []
    for i in list(set([item for sublist in line for item in sublist]) - set(line[z])):
      a = i.replace("+1", "1").replace("-1", "0").strip("\n").split()
      sent = []
      for j in a:
        j = stemmer.stemWord(j)
        if j not in get_stop_words("english"):
          sent.append(j)
      data.append(sent)

    a = train(data)

    tp = 0
    fp = 0
    fn = 0
    tn = 0

    for i in line[z]:
      rate = predict(a, i[3:-1].split())
      if rate > thr:
        tag = "+1"
      else:
        tag = "-1"
      if tag == "+1" and i[:2] == "+1":
        tp += 1 
      elif tag == "+1" and i[:2] == "-1":
        fp += 1 
      elif tag == "-1" and i[:2] == "+1":
        fn += 1 
      elif tag == "-1" and i[:2] == "-1":
        tn += 1 

    precision.append(tp / (tp + fp))
    recall.append(tp / (tp + fn))

  precisions.append(sum(precision) / 5)
  recalls.append(sum(recall) / 5)

x = np.arange(0.02, 1.0, 0.05)
plt.plot(x, precisions, x, recalls)
plt.show() 
