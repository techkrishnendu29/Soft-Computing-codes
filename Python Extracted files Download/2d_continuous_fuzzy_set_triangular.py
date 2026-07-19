#representation of discrete fuzzy sets
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
# Triangular Membership Function
mu = np.maximum(0, np.minimum(x/5, (10-x)/5))
plt.plot(x, mu)
plt.xlabel("Universe of Discourse")
plt.ylabel("Membership Value")
plt.title("Continuous Fuzzy Set (Triangular MF)")
plt.show()
