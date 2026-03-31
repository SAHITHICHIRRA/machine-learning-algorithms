from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y = iris.target

plt.scatter(X[:,0],X[:,2],c=y)

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.show()
