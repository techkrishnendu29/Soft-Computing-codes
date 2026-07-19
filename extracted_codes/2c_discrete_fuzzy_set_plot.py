import matplotlib.pyplot as plt
elements = [1, 2, 3, 4, 5]
membership = [0.1, 0.3, 0.6, 0.8, 1.0]
plt.stem(elements, membership)
plt.xlabel("Elements")
plt.ylabel("Membership Value")
plt.title("Discrete Fuzzy Set Representation")
plt.show()
