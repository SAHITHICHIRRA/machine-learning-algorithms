height = np.array([150,155,160,165,170,175])
weight = np.array([50,55,60,68,72,78])

h_mean = np.mean(height)
h_std = np.std(height)

w_mean = np.mean(weight)
w_std = np.std(weight)

height_z = (height - h_mean) / h_std
weight_z = (weight - w_mean) / w_std

print(height_z)
print(weight_z)
