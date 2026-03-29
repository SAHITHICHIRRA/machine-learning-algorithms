import numpy as np

height = np.array([150,155,160,165,170])
weight = np.array([50,55,60,65,72])

height_m = height / 100

bmi = weight / (height_m ** 2)

print("BMI:", bmi)
