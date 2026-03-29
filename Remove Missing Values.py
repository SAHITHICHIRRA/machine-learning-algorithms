mask = ~np.isnan(study_hours) & ~np.isnan(marks)

clean_hours = study_hours[mask]
clean_marks = marks[mask]

print("Clean Hours:", clean_hours)
print("Clean Marks:", clean_marks)

print("New Mean Hours:", np.mean(clean_hours))
print("New Mean Marks:", np.mean(clean_marks))

plt.scatter(clean_hours, clean_marks)
plt.show()
