import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

housing = fetch_california_housing()

X = housing.data
y = housing.target

splits = [0.3,0.2,0.1]

mse_values = []
r2_values = []

for split in splits:

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=split)

    model = LinearRegression()
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test,y_pred)
    r2 = r2_score(y_test,y_pred)

    mse_values.append(mse)
    r2_values.append(r2)

    print("\nSplit:", 1-split,"train")
    print("MSE:",mse)
    print("R2:",r2)

# Plot
train_sizes = [70,80,90]

plt.plot(train_sizes, r2_values, marker='o')

plt.xlabel("Training Size (%)")
plt.ylabel("R2 Score")
plt.title("Model Stability")

plt.show()
