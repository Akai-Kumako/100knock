#98. Ward法によるクラスタリング

import pickle
import numpy as np
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

with open("nations_vec.pickle", "rb") as f:
  vecs = pickle.load(f)

features = np.empty([0, 300], dtype=np.float64)

for value in vecs.values():
  features = np.vstack([features, value])

ward = ward(features)
print(ward)

dendrogram(ward, labels=list(vecs.keys()), leaf_font_size=8)
plt.show()
