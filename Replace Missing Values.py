hours_mean = np.nanmean(study_hours)
marks_mean = np.nanmean(marks)

study_hours[np.isnan(study_hours)] = hours_mean
marks[np.isnan(marks)] = marks_mean

plt.scatter(study_hours, marks)
plt.show()
