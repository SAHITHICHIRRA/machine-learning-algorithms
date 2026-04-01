import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load dataset
housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['Price'] = housing.target

print(df.head())

X = df.drop('Price',axis=1)
y = df['Price']

# Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train,y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print("RMSE:",rmse)
print("R2:",r2)

# Coefficients
coeff = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\nFeature Importance")
print(coeff)
