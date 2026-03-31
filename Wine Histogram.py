from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

wine = load_wine()

alcohol = wine.data[:,0]

plt.hist(alcohol,bins=20)

plt.title("Alcohol Distribution")

plt.show()
