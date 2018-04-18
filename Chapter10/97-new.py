#97. k-meansクラスタリング

import pickle
import numpy as np
from sklearn.cluster import KMeans

with open("nations_vec.pickle", "rb") as f:
  vecs = pickle.load(f)

features = np.empty([0, 300], dtype=np.float64)

for value in vecs.values():
  features = np.vstack([features, value])

clusters = KMeans(n_clusters=5).fit_predict(features)

result = zip(vecs.keys(), clusters)

for country, category in sorted(result, key=lambda x: x[1]):
    print('{}\t{}'.format(category, country))
