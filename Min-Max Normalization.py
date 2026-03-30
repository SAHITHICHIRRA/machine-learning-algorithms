hours_norm = (hours - hours.min()) / (hours.max() - hours.min())
att_norm = (attendance - attendance.min()) / (attendance.max() - attendance.min())

plt.plot(hours_norm)
plt.plot(att_norm)
plt.show()
