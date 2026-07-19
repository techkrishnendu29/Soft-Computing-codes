import numpy as np
# XOR Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([
    [0],
    [1],
    [1],
    [0]
])
# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Derivative of Sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)
# Learning Parameters
learning_rate = 0.4
epochs = 2000
# Initialize Weights and Biases
np.random.seed(1)
W1 = np.random.randn(2, 2) # Input to Hidden
B1 = np.zeros((1, 2))
W2 = np.random.randn(2, 1) # Hidden to Output
B2 = np.zeros((1, 1))
# Training
for epoch in range(epochs):
    # ---------- Forward Propagation ----------
    hidden_input = np.dot(X, W1) + B1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, W2) + B2
    final_output = sigmoid(final_input)
    # ---------- Error ----------
    error = y - final_output
    # ---------- Backpropagation ----------
    output_delta = error * sigmoid_derivative(final_output)
    hidden_error = np.dot(output_delta, W2.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
    # ---------- Update Weights ----------
    W2 += learning_rate * np.dot(hidden_output.T, output_delta)
    B2 += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    W1 += learning_rate * np.dot(X.T, hidden_delta)
    B1 += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)
    # Display Loss Every 1000 Epochs
    if (epoch + 1) % 1000 == 0:
        loss = np.mean(error ** 2)
        print(f"Epoch {epoch+1}, Loss = {loss:.4f}")
# Testing
print("\nFinal Predictions:")
hidden = sigmoid(np.dot(X, W1) + B1)
output = sigmoid(np.dot(hidden, W2) + B2)
prediction = np.round(output)
print(prediction)
print("\nActual Output:")
print(y)
