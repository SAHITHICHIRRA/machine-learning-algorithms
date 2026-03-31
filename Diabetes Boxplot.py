from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

diabetes = load_diabetes()

feature = diabetes.data[:,2]

plt.boxplot(feature)

plt.title("Feature Boxplot")

plt.show()
