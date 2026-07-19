import numpy as np
import matplotlib.pyplot as plt
# Triangular membership function
def triangle(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)
# Define fuzzy sets
sets = [(0, 2, 4), (3, 5, 7)]
x = np.linspace(0, 7, 500)
total_area = 0
weighted_sum = 0
plt.figure()
for a, b, c in sets:
    mu = triangle(x, a, b, c)
    plt.plot(x, mu)
    # Area and centroid
    area = 0.5 * (c - a)
    centroid = b
    total_area += area
    weighted_sum += area * centroid
# Center of Sum crisp value
cos_value = weighted_sum / total_area
# Plot crisp output
plt.axvline(cos_value)
plt.scatter(cos_value, 0)
plt.title("Center of Sum Defuzzification")
plt.xlabel("x")
plt.ylabel("Membership μ(x)")
plt.ylim(0, 1.1)
plt.grid()
