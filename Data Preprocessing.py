import numpy as np
import matplotlib.pyplot as plt

study_hours = np.array([2,4,6,np.nan,8,10,25])
marks = np.array([35,45,55,60,np.nan,85,95])

mean_hours = np.nanmean(study_hours)
mean_marks = np.nanmean(marks)

print("Mean hours:", mean_hours)
print("Mean marks:", mean_marks)

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
