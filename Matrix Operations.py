import numpy as np

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print("Determinant:", np.linalg.det(A))

print("Addition:\n", A + B)

print("Subtraction:\n", A - B)

print("Multiplication:\n", A * B)

print("Division:\n", A / B)

print("Transpose:\n", A.T)

print("Dot Product:\n", np.dot(A,B))

print("Cross Product:", np.cross([1,2,3],[4,5,6]))
