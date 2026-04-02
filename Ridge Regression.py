from sklearn.linear_model import Ridge

X = df[['Area','Bedrooms','Age']]
y = df['Price']

ridge = Ridge(alpha=1.0)

ridge.fit(X,y)

pred = ridge.predict(X)

rmse = np.sqrt(mean_squared_error(y,pred))

SSE = np.sum((y-pred)**2)
SST = np.sum((y-np.mean(y))**2)
SSR = SST - SSE

print("RMSE:",rmse)
print("SSE:",SSE)
print("SST:",SST)
print("SSR:",SSR)
