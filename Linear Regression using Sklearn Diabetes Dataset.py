import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
diabetes = load_diabetes()

X = diabetes.data[:, 2]   # one feature
y = diabetes.target

X = X.reshape(-1,1)

# Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train,y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("MSE:",mse)
print("R2 Score:",r2)

# Plot
plt.scatter(X_test,y_test)
plt.plot(X_test,y_pred)

plt.xlabel("Feature")
plt.ylabel("Target")

plt.show()
