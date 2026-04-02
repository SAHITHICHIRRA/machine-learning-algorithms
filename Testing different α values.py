alphas = [0.1,1,10,100]

for a in alphas:
    model = Ridge(alpha=a)
    model.fit(X,y)
    pred = model.predict(X)
    rmse = np.sqrt(mean_squared_error(y,pred))
    print("Alpha:",a,"RMSE:",rmse)
