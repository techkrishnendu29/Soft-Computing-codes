import numpy as np
import matplotlib.pyplot as plt
# trapezoidal membership function
def trapezoid(x, a, b, c, d, height=1):
    return height * np.maximum(
        np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)),
        0
    )
# trapezoid centroid
def trap_centroid(a, b, c, d):
    return (a + 2*b + 2*c + d) / 6
# domain
x = np.linspace(0, 10, 1000)
# weights
w1 = 0.7
w2 = 0.5
# trapezoidal sets
mu1 = trapezoid(x, 1, 2, 4, 5, w1)
mu2 = trapezoid(x, 4, 6, 8, 9, w2)
# centroids
c1 = trap_centroid(1, 2, 4, 5)
c2 = trap_centroid(4, 6, 8, 9)
# weighted average
wa = (w1*c1 + w2*c2) / (w1 + w2)
# plotting
plt.figure()
plt.plot(x, mu1, linestyle="--", label="Trapezoid A1")
plt.plot(x, mu2, linestyle="--", label="Trapezoid A2")
plt.fill_between(x, mu1, alpha=0.3)
plt.fill_between(x, mu2, alpha=0.3)
plt.axvline(wa, linestyle=":", label="Weighted Average")
plt.title("Weighted Average — Two Trapezoidal Sets")
plt.xlabel("x")
plt.ylabel("Membership μ(x)")
plt.legend()
plt.grid()
plt.show()
print("Centroid A1 =", round(c1,3))
print("Centroid A2 =", round(c2,3))
print("Defuzzified value =", round(wa,3))
