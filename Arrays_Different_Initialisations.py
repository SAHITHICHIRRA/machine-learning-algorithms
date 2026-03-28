import numpy as np

a = np.random.rand(5)
b = np.random.rand(3,3)

print("Random 1D:", a)
print("Random 2D:\n", b)


c = np.zeros(5)
d = np.zeros((3,3))

print("\nDefault 1D:", c)
print("Default 2D:\n", d)


print("\nDiagonal:", np.diag(d))


print("First element:", b[0][0])


print("Last element:", b[-1][-1])


print("Second row:", b[1])


print("Second column:", b[:,1])


print("Number of elements:", b.size)
