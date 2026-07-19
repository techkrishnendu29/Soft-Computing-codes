import numpy as np
import matplotlib.pyplot as plt
# triangular membership function
def triangle(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)
# domain
x = np.linspace(0, 10, 2000)
# fuzzy sets
mu1 = triangle(x, 1, 3, 5)
mu2 = triangle(x, 4, 6, 9)
# aggregation
mu = np.maximum(mu1, mu2)
# numerical integration (area)
dx = x[1] - x[0]
cumulative_area = np.cumsum(mu) * dx
total_area = cumulative_area[-1]
# find bisector index
bisector_index = np.where(cumulative_area >= total_area/2)[0][0]
boa = x[bisector_index]
# plotting
plt.figure()
plt.plot(x, mu1, linestyle="--", label="Triangle A1")
plt.plot(x, mu2, linestyle="--", label="Triangle A2")
plt.plot(x, mu, linewidth=2, label="Aggregated")
plt.fill_between(x, mu, alpha=0.3)
plt.axvline(boa, linestyle=":", label="Area Bisector")
plt.title("Area Bisector Defuzzification")
plt.xlabel("x")
plt.ylabel("Membership μ(x)")
plt.legend()
plt.grid()
plt.show()
print("Defuzzified value (Area Bisector) =", round(boa, 3))
