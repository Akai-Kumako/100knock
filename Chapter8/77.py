 #77. 正解率の計測

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

def predict(dic, word_list):
    cnt = 0.
    for word in word_list:
        word = (word)
        if word in dic:
            cnt += dic[word]
    rate = (1. / (1. + math.exp(-cnt)))
    return rate

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

tp = 0
fp = 0
fn = 0
tn = 0

with open("sentiment.txt") as f:
  for i in f:
    rate = predict(a, i[3:-1].split())
    if rate > 0.5:
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

accuracy = (tp + tn) / (tp + fp + fn + tn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
fscore = (2 * recall * precision) / (recall + precision)

print("正解率: {}".format(accuracy))
print("適合率: {}".format(precision))
print("再現率: {}".format(recall))
print("F1スコア: {}".format(fscore))
