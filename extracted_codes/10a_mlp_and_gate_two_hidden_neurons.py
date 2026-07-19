import numpy as np
# AND Gate Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([[0],
              [0],
              [0],
              [1]])
# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Derivative of Sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)
# Parameters
learning_rate = 0.5
epochs = 10000
# Initialize weights and biases
np.random.seed(1)
hidden_weights = np.random.randn(2, 2)
hidden_bias = np.random.randn(1, 2)
output_weights = np.random.randn(2, 1)
output_bias = np.random.randn(1, 1)
# Training
for epoch in range(epochs):
    # ---------- Forward Pass ----------
    hidden_input = np.dot(X, hidden_weights) + hidden_bias
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, output_weights) + output_bias
    predicted_output = sigmoid(final_input)
    # ---------- Backpropagation ----------
    error = y - predicted_output
    output_delta = error * sigmoid_derivative(predicted_output)
    hidden_error = np.dot(output_delta, output_weights.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
    # ---------- Update Weights ----------
    output_weights += learning_rate * np.dot(hidden_output.T, output_delta)
    output_bias += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    hidden_weights += learning_rate * np.dot(X.T, hidden_delta)
    hidden_bias += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)
# Testing
print("Final Output")
for i in range(len(X)):
    hidden = sigmoid(np.dot(X[i], hidden_weights) + hidden_bias)
    output = sigmoid(np.dot(hidden, output_weights) + output_bias)
    prediction = 1 if output >= 0.5 else 0
    print("Input:", X[i], "Output:", prediction)
