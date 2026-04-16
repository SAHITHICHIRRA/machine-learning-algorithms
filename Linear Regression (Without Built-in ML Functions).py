# Linear Regression from scratch

x = [1,2,3,4,5]
y = [2,4,5,4,5]

n = len(x)

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

# prediction
x_test = 6
y_pred = m * x_test + b
print("Predicted value:", y_pred)
