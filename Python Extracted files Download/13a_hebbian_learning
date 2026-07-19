import numpy as np
# Function to train using Hebbian Learning Rule
def hebbian_train(X, Y, learning_rate=1):
    # Initialize weights and bias
    n_features = X.shape[1]
    w = np.zeros(n_features)
    b = 0
    # Training
    for i in range(len(X)):
        w = w + learning_rate * X[i] * Y[i]
        b = b + learning_rate * Y[i]
    return w, b
# Function to test the model
def hebbian_predict(X, w, b):
    net = np.dot(X, w) + b
    return np.sign(net)
# -------------------------
# Static Training Data
# -------------------------
X = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])
Y = np.array([
    1,
    -1,
    -1,
    -1
])
# -------------------------
# Training
# -------------------------
w, b = hebbian_train(X, Y)
print("Final Weights:", w)
print("Bias:", b)
# -------------------------
# Static Test Data
# -------------------------
test_samples = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])
print("\nTesting Phase")
for sample in test_samples:
    output = hebbian_predict(sample, w, b)
    print(f"Input: {sample} -> Predicted Output: {int(output)}")
