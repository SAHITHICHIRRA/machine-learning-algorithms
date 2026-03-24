
n = int(input("Enter number of data points: "))

x = []
y = []

print("Enter x values:")
for i in range(n):
    val = float(input())
    x.append(val)

print("Enter y values:")
for i in range(n):
    val = float(input())
    y.append(val)

sum_x = sum(x)
sum_y = sum(y)

sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]


m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
b = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (b):", b)


x_test = float(input("Enter value of x for prediction: "))
y_pred = m * x_test + b

print("Predicted value:", y_pred)
