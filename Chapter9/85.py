#85. 主成分分析による次元圧縮

from scipy import io, sparse
import sklearn.decomposition

det = io.loadmat("WCmatrix")["det"]
com = sklearn.decomposition.TruncatedSVD(300).fit_transform(det)

io.savemat("WCmatrix_X", {"com":com})
