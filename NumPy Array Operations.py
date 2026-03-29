import numpy as np

arr = np.array([45, 50, 55, 60, 65, 70, 75, 80])

add5 = arr + 5
print("After adding 5:", add5)

mul2 = arr * 2
print("After multiplying by 2:", mul2)

mean = np.mean(arr)
std = np.std(arr)

print("Mean:", mean)
print("Standard Deviation:", std)
