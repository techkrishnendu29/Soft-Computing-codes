import numpy as np
import matplotlib.pyplot as plt
# Trapezoidal membership function
def trapezoid(x, a, b, c, d):
    return np.maximum(
        np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)),
        0
    )
# Two trapezoidal fuzzy sets
A1 = (0, 1, 3, 4)
A2 = (2, 4, 6, 7)
sets = [A1, A2]
x = np.linspace(0, 7, 500)
total_area = 0
weighted_sum = 0
plt.figure()
for a, b, c, d in sets:
    mu = trapezoid(x, a, b, c, d)
    plt.plot(x, mu)
    # trapezoid area
    area = ((b-a) + (d-c) + 2*(c-b)) / 2
    # centroid approximation
    centroid = (b + c) / 2
    total_area += area
    weighted_sum += area * centroid
# COS crisp value
cos_value = weighted_sum / total_area
# Plot crisp result
plt.axvline(cos_value)
plt.scatter(cos_value, 0)
plt.title("Center of Sum — 2 Trapezoidal Fuzzy Sets")
plt.xlabel("x")
plt.ylabel("Membership μ(x)")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
print("Defuzzified value (COS):", round(cos_value, 3))
