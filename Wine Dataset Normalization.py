from sklearn.datasets import load_wine
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

wine = load_wine()

X = wine.data[:,0]

scaler = MinMaxScaler()

X_norm = scaler.fit_transform(X.reshape(-1,1))

plt.plot(X,label="Original")
plt.plot(X_norm,label="Normalized")

plt.legend()
plt.show()
