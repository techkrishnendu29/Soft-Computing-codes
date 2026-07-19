import matplotlib.pyplot as plt
# Given fuzzy set
x_vals = [0, 1, 2, 3, 4, 5]
mu_vals = [0.1, 0.4, 0.8, 1.0, 0.6, 0.2]
# Multiple lambda values
lambdas = [0.2, 0.4, 0.6, 0.8]
plt.figure()
plt.plot(x_vals, mu_vals, marker='o', label="Fuzzy set")
for lam in lambdas:
    cut_x = [x for x, mu in zip(x_vals, mu_vals) if mu >= lam]
    if cut_x:
        x_left = min(cut_x)
        x_right = max(cut_x)
        midpoint = (x_left + x_right) / 2
        print(f"\nλ = {lam}")
        print("Elements:", cut_x)
        print("Interval:", [x_left, x_right])
        print("Midpoint:", midpoint)
        # draw lambda line
        plt.axhline(lam, linestyle='--')
# Graph formatting
plt.xlabel("x")
plt.ylabel("Membership μ(x)")
plt.title("Multiple Lambda-Cut Method")
plt.ylim(0, 1.1)
plt.grid()
plt.legend()
plt.show()
