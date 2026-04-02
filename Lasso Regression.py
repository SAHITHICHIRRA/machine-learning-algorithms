from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
import numpy as np

X = df[['Area','Bedrooms','Age']]
y = df['Price']

lasso = Lasso(alpha=0.1)

lasso.fit(X,y)

pred = lasso.predict(X)

rmse = np.sqrt(mean_squared_error(y,pred))
r2 = r2_score(y,pred)

print("RMSE:",rmse)
print("R2 Score:",r2)
