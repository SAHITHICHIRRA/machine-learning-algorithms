import matplotlib.pyplot as plt

plt.scatter(df['Sleep_Hours'],df['Alert'])
plt.xlabel("Sleep Hours")
plt.ylabel("Alert")
plt.show()
