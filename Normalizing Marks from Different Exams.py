test1 = np.array([35,40,45,48])
test2 = np.array([60,70,80,90])

plt.plot(test1)
plt.plot(test2)
plt.show()

# normalization

test1_norm = (test1-test1.min())/(test1.max()-test1.min())
test2_norm = (test2-test2.min())/(test2.max()-test2.min())

plt.plot(test1_norm)
plt.plot(test2_norm)
plt.show()
