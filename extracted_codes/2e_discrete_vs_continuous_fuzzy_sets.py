# Comparing Discrete and Continuous Fuzzy Sets
import numpy as np
import matplotlib.pyplot as plt
# Discrete
x_d = [1, 2, 3, 4, 5]
mu_d = [0.2, 0.4, 0.6, 0.8, 1.0]
# Continuous
x_c = np.linspace(0, 5, 100)
mu_c = x_c / 5
plt.stem(x_d, mu_d)
plt.plot(x_c, mu_c)
plt.xlabel("Elements")
plt.ylabel("Membership Value")
plt.title("Discrete vs Continuous Fuzzy Sets")
plt.show()
