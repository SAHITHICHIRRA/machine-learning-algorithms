import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler

data = np.array([[150,50],[155,55],[160,60],[165,90],[170,95]])

minmax = MinMaxScaler()
std = StandardScaler()

norm = minmax.fit_transform(data)
standard = std.fit_transform(data)

plt.scatter(norm[:,0],norm[:,1])
plt.title("Normalized Data")
plt.show()

plt.scatter(standard[:,0],standard[:,1])
plt.title("Standardized Data")
plt.show()
