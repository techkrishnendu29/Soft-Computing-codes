import numpy as np
import matplotlib.pyplot as plt
# -------- RANDOM DATA --------
np.random.seed(42)
n = 50
m = 2
X = np.random.rand(n, m)
# -------- SOM PARAMETERS --------
grid_size = 3
learning_rate = 0.5
epochs = 100
weights = np.random.rand(grid_size, grid_size, m)
# -------- FUNCTIONS --------
def euclidean(x, w):
    return np.linalg.norm(x - w)
def find_bmu(x):
    min_dist = float('inf')
    bmu = (0, 0)
    for i in range(grid_size):
        for j in range(grid_size):
            dist = euclidean(x, weights[i][j])
            if dist < min_dist:
                min_dist = dist
                bmu = (i, j)
    return bmu
# -------- TRAINING --------
for epoch in range(epochs):
    for x in X:
        bmu_i, bmu_j = find_bmu(x)
        for i in range(grid_size):
            for j in range(grid_size):
                dist_to_bmu = np.linalg.norm([i - bmu_i, j - bmu_j])
                sigma = np.exp(-epoch / epochs)
                h = np.exp(-(dist_to_bmu**2) / (2 * sigma**2))
                weights[i][j] += learning_rate * h * (x - weights[i][j])
    learning_rate *= 0.9
# -------- CLUSTER ASSIGNMENT --------
clusters = {}
for i in range(grid_size):
    for j in range(grid_size):
        clusters[(i, j)] = []
for x in X:
    bmu = find_bmu(x)
    clusters[bmu].append(x)
# -------- PLOTTING --------
plt.figure()
# Plot each cluster separately (auto colors)
for key, points in clusters.items():
    if len(points) > 0:
        points = np.array(points)
        plt.scatter(points[:, 0], points[:, 1], label=f"Cluster {key}")
# Plot neurons
for i in range(grid_size):
    for j in range(grid_size):
        w = weights[i][j]
        plt.scatter(w[0], w[1], marker='x')
        plt.text(w[0], w[1], f"N({i},{j})")
plt.title("Kohonen SOM Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid()
plt.show()
