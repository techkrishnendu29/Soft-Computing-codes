# 1st Order Sugeno Fuzzy Model with Plots
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# -----------------------------
# Triangular Membership Function
# -----------------------------
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)
# -----------------------------
# Input Range
# -----------------------------
x = np.linspace(0, 10, 200)
y = np.linspace(0, 10, 200)
# -----------------------------
# Membership Functions for X
# -----------------------------
mu_A1 = triangular(x, 0, 3, 6)
mu_A2 = triangular(x, 4, 7, 10)
plt.figure()
plt.plot(x, mu_A1)
plt.plot(x, mu_A2)
plt.xlabel("Input X")
plt.ylabel("Membership Degree")
plt.title("Membership Functions for X")
plt.grid(True)
plt.show()
# -----------------------------
# Membership Functions for Y
# -----------------------------
mu_B1 = triangular(y, 0, 3, 6)
mu_B2 = triangular(y, 4, 7, 10)
plt.figure()
plt.plot(y, mu_B1)
plt.plot(y, mu_B2)
plt.xlabel("Input Y")
plt.ylabel("Membership Degree")
plt.title("Membership Functions for Y")
plt.grid(True)
plt.show()
# -----------------------------
# Sugeno 3D Output Surface
# -----------------------------
X, Y = np.meshgrid(x, y)
mu_A1_2D = triangular(X, 0, 3, 6)
mu_A2_2D = triangular(X, 4, 7, 10)
mu_B1_2D = triangular(Y, 0, 3, 6)
mu_B2_2D = triangular(Y, 4, 7, 10)
# Rule firing strengths
w1 = mu_A1_2D * mu_B1_2D
w2 = mu_A2_2D * mu_B2_2D
# First-order Sugeno outputs
z1 = 2*X + Y + 1
z2 = X + 2*Y + 2
# Final Output (Weighted Average)
Z = (w1*z1 + w2*z2) / (w1 + w2 + 1e-6)
# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel("Input X")
ax.set_ylabel("Input Y")
ax.set_zlabel("Output Z")
ax.set_title("1st Order Sugeno Output Surface")
plt.show()
