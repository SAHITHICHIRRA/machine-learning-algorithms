import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Excel file
data = pd.read_excel("student_scores.xlsx")

print("Dataset:")
print(data)

# Data cleaning
print("\nMissing values:")
print(data.isnull().sum())

# Extract values
X = data['study_hours'].values
Y = data['marks'].values

n = len(X)

# Calculate slope (m) and intercept (c)
m = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y)) / (n*np.sum(X**2) - (np.sum(X))**2)
c = (np.sum(Y) - m*np.sum(X)) / n

print("\nSlope:", m)
print("Intercept:", c)

# Prediction function
def predict(x):
    return m*x + c

# Predict marks for new student
new_hours = 9
predicted_marks = predict(new_hours)

print("\nPredicted Marks for 9 hours:", predicted_marks)

# Plot
plt.scatter(X, Y, color='blue', label="Actual Data")
plt.plot(X, predict(X), color='red', label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression")
plt.legend()

plt.show()
