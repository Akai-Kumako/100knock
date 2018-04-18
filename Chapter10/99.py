#99. t-SNEによる可視化

import pickle
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open("nations_vec.pickle", "rb") as f:
  vecs = pickle.load(f)

features = np.empty([0, 300], dtype=np.float64)

for value in vecs.values():
  features = np.vstack([features, value])

tsne = TSNE().fit_transform(features)

clusters = KMeans(n_clusters=5).fit_predict(features)

fig, ax = plt.subplots()
cmap = plt.get_cmap("Set1")
for vecs, label in enumerate(vecs.keys()):
    cval = cmap(clusters[vecs] / 4)
    ax.scatter(tsne[vecs, 0], tsne[vecs, 1], marker='.', color=cval)
    ax.annotate(label, xy=(tsne[vecs, 0], tsne[vecs, 1]), color=cval)
plt.show()
