import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
data = pd.read_csv("salary_data.csv")

print(data.head())

# Data inspection
print("\nInfo:")
print(data.info())

X = data[['experience']]
y = data['salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction
new_exp = [[5.5]]
pred_salary = model.predict(new_exp)

print("\nPredicted Salary:", pred_salary)

# Predictions for dataset
y_pred = model.predict(X)

# Evaluation
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("MAE:", mae)
print("MSE:", mse)

# Plot
plt.scatter(X, y)
plt.plot(X, y_pred)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction")

plt.show()
