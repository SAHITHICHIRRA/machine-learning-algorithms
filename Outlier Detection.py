study_hours = np.array([2,4,6,8,10,25])

mean_with = np.mean(study_hours)

without_outlier = study_hours[study_hours != 25]
mean_without = np.mean(without_outlier)

print("Mean with outlier:", mean_with)
print("Mean without outlier:", mean_without)
