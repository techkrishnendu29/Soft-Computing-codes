import numpy as np
x = np.array([1, 2, 3, 4, 5])
A = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
for i in range(len(x)):
    print(f"x={x[i]} mA={A[i]}")
