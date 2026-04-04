import numpy as np
from sklearn.linear_model import Ridge

n = int(input("Enter number of samples: "))

X = []
y = []

print("Enter x1 x2 and y")

for i in range(n):
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    target = float(input("Enter y: "))

    X.append([x1, x2])
    y.append(target)

X = np.array(X)
y = np.array(y)

alpha = float(input("Enter Ridge regularization value (alpha): "))

model = Ridge(alpha=alpha)

model.fit(X, y)

print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

x1 = float(input("\nEnter new x1: "))
x2 = float(input("Enter new x2: "))

prediction = model.predict([[x1, x2]])

print("Predicted value:", prediction[0])
