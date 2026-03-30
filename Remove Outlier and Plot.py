hours = np.array([2,4,6,8,10,25])
marks = np.array([35,45,55,60,85,95])

hours_clean = hours[hours != 25]
marks_clean = marks[:5]

plt.scatter(hours_clean, marks_clean)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("After Removing Outlier")

plt.show()
