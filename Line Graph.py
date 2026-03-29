import matplotlib.pyplot as plt
import numpy as np

marks = np.array([50,55,60,65,72])

plt.plot(marks)

plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Student Marks Line Graph")

plt.show()
