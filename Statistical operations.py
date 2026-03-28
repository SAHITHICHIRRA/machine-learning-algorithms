import numpy as np
from scipy import stats

a = np.array([1,2,3,4,5,6,7])

print("Min:", np.min(a))
print("Max:", np.max(a))
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Mode:", stats.mode(a))
print("Standard Deviation:", np.std(a))
