import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)
# One-hot encoding
encoder = OneHotEncoder(sparse_output=False) # Changed 'sparse' to 'sparse_output'
y = encoder.fit_transform(y)
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Normalize
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Network architecture
input_size = 4
hidden_size = 5
output_size = 3
# Initialize weights
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))
# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
def softmax(x):
    exp = np.exp(x - np.max(x))
    return exp / exp.sum(axis=1, keepdims=True)
# Training
learning_rate = 0.01
epochs = 1000
for epoch in range(epochs):
    # Forward pass
    Z1 = np.dot(X_train, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = softmax(Z2)
    # Loss (optional print)
    loss = -np.mean(y_train * np.log(A2 + 1e-8))
    # Backward pass
    dZ2 = A2 - y_train
    dW2 = np.dot(A1.T, dZ2)
    db2 = np.sum(dZ2, axis=0, keepdims=True)
    dZ1 = np.dot(dZ2, W2.T) * sigmoid_derivative(A1)
    dW1 = np.dot(X_train.T, dZ1)
    db1 = np.sum(dZ1, axis=0, keepdims=True)
    # Update weights
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")
# Testing
Z1 = np.dot(X_test, W1) + b1
A1 = sigmoid(Z1)
Z2 = np.dot(A1, W2) + b2
A2 = softmax(Z2)
predictions = np.argmax(A2, axis=1)
actual = np.argmax(y_test, axis=1)
accuracy = np.mean(predictions == actual)
print("\nAccuracy:", accuracy)
