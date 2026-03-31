import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = np.array([[20000,20],[40000,30],[60000,40]])

scaler = MinMaxScaler()

scaled = scaler.fit_transform(data)

print(scaled)
