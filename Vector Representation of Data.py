import numpy as np

study_hours = np.array([2,4,6,8,10])
marks = np.array([40,50,60,75,90])

# feature matrix
X = np.column_stack((study_hours,marks))

print("Feature Matrix:")
print(X)
