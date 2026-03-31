from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
import numpy as np

data = load_breast_cancer()

X = data.data

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("Mean:",np.mean(X_scaled))
print("Std:",np.std(X_scaled))
