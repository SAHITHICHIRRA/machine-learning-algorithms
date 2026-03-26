import random
import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

# user inputs --
x1 = float(input("Enter first input: "))
x2 = float(input("Enter second input: "))

X = [x1,x2]

target = float(input("Enter target output: "))

# random weights --
w1 = random.random()
w2 = random.random()
w3 = random.random()

learning_rate = 0.5

epochs = int(input("Enter number of epochs: "))

for epoch in range(epochs):

    # forward propagation --
    hidden = sigmoid(X[0]*w1 + X[1]*w2)
    output = sigmoid(hidden*w3)

    # error
    error = target - output

    # backpropagation
    d_output = error * sigmoid_derivative(output)

    d_hidden = d_output * w3 * sigmoid_derivative(hidden)

    # weight updates
    w3 += learning_rate * d_output * hidden
    w1 += learning_rate * d_hidden * X[0]
    w2 += learning_rate * d_hidden * X[1]

print("\nTrained Weights:")
print("w1 =",round(w1,4))
print("w2 =",round(w2,4))
print("w3 =",round(w3,4))

print("Predicted Output =",round(output,4))
