import numpy as np
# Activation function (step)
def step(x):
    return 1 if x >= 0 else 0
# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
T = np.array([0, 1, 1, 0])
# Learning rate
eta = 0.1
epochs = 20
# Initialize weights (random)
np.random.seed(1)
# Hidden layer (2 neurons)
w_hidden = np.random.randn(2, 2) # 2 neurons, 2 inputs
b_hidden = np.random.randn(2)
# Output layer
w_out = np.random.randn(2)
b_out = np.random.randn(1)
# Training using Delta Rule
for epoch in range(epochs):
    print(f"\nEpoch {epoch+1}")
    for i in range(len(X)):
        x = X[i]
        t = T[i]
        # ---- Forward pass ----
        z_in = np.dot(w_hidden, x) + b_hidden
        z = np.array([step(z_in[0]), step(z_in[1])])
        y_in = np.dot(w_out, z) + b_out
        y = step(y_in)
        # ---- Error ----
        error = t - y
        # ---- Delta Rule Updates ----
        # Output layer update
        w_out = w_out + eta * error * z
        b_out = b_out + eta * error
        # Hidden layer update (approximate Madaline Rule)
        for j in range(2):
            w_hidden[j] = w_hidden[j] + eta * error * x
            b_hidden[j] = b_hidden[j] + eta * error
# ---- Testing ----
print("\nFinal Output:")
print("x1 x2 | Output")
print("----------------")
for i in range(len(X)):
    x = X[i]
    z = np.array([
        step(np.dot(w_hidden[0], x) + b_hidden[0]),
        step(np.dot(w_hidden[1], x) + b_hidden[1])
    ])
    y = step(np.dot(w_out, z) + b_out)
    print(f"{x[0]} {x[1]} | {y}")
