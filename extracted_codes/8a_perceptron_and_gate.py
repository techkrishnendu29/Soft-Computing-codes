import numpy as np
# Training data (AND gate example)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
# Target output
y = np.array([0, 0, 0, 1])
# Initialize weights and bias
weights = np.zeros(2)
bias = 0
learning_rate = 0.1
epochs = 10
# Activation function
def activation(z):
    if z >= 0:
        return 1
    else:
        return 0
# Training the perceptron
for epoch in range(epochs):
    print("Epoch:", epoch+1)
    for i in range(len(X)):
        z = np.dot(X[i], weights) + bias
        y_pred = activation(z)
        error = y[i] - y_pred
        # Update weights and bias
        weights = weights + learning_rate * error * X[i]
        bias = bias + learning_rate * error
        print("Input:", X[i], "Predicted:", y_pred, "Error:", error)
print("\nFinal Weights:", weights)
print("Final Bias:", bias)
# Testing the perceptron
print("\nTesting")
for i in range(len(X)):
    z = np.dot(X[i], weights) + bias
    y_pred = activation(z)
    print(X[i], "->", y_pred)
