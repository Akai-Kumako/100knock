#99. t-SNEによる可視化

import pickle
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open("nations_vec.pickle", "rb") as f:
  vecs = pickle.load(f)

features = np.empty([0, 300], dtype=np.float64)

for value in vecs.values():
  features = np.vstack([features, value])

tsne = TSNE(n_components=3).fit_transform(features)

x = np.arange(-100, 100, 0.25)
y = np.arange(-100, 100, 0.25)

X, Y = np.meshgrid(x, y)
Z = np.sin(X)+ np.cos(Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z)

plt.show()

print(tsne)
