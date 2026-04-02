import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# dataset
data = {
'Area':[1000,1500,1800,2400,3000],
'Bedrooms':[2,3,3,4,4],
'Age':[20,15,18,30,8],
'Price':[300000,450000,500000,650000,700000]
}

df = pd.DataFrame(data)

# Independent variables
X = df[['Area','Bedrooms','Age']]

# Target variable
y = df['Price']

# Model
model = LinearRegression()

# Train model
model.fit(X,y)

# Predictions
predictions = model.predict(X)

# Evaluation metrics
rmse = np.sqrt(mean_squared_error(y,predictions))

SSE = np.sum((y-predictions)**2)
SST = np.sum((y-np.mean(y))**2)
SSR = SST - SSE

print("RMSE:",rmse)
print("SSE:",SSE)
print("SST:",SST)
print("SSR:",SSR)

# Visualization
plt.scatter(y,predictions)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.show()
