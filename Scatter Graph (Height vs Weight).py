import matplotlib.pyplot as plt
import numpy as np

height = np.array([150,155,160,165,170])
weight = np.array([50,55,60,65,72])

plt.scatter(height, weight)

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")

plt.show()
