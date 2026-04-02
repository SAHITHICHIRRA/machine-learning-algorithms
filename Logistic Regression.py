import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
'Sleep_Hours':[3,4,5,6,7,8],
'Alert':[0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Sleep_Hours']]
y = df['Alert']

model = LogisticRegression()

model.fit(X,y)

prediction = model.predict([[5]])

prob = model.predict_proba([[5]])

print("Predicted Label:",prediction[0])
print("Probability:",prob)
