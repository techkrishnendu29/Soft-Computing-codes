import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
# Gaussian Membership Function
mu = np.exp(-((x - 5) ** 2) / 2)
plt.plot(x, mu)
plt.xlabel("Universe of Discourse")
plt.ylabel("Membership Value")
plt.title("Continuous Fuzzy Set (Gaussian MF)")
plt.show()
