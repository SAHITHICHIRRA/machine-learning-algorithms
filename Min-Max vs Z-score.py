import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler

X = np.array([[10],[20],[30],[100]])

minmax = MinMaxScaler()
zscore = StandardScaler()

X_minmax = minmax.fit_transform(X)
X_zscore = zscore.fit_transform(X)

plt.plot(X,label="Original")
plt.plot(X_minmax,label="MinMax")
plt.plot(X_zscore,label="ZScore")

plt.legend()
plt.show()
