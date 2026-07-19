import matplotlib.pyplot as plt
# Given fuzzy set (x values and memberships)
x_vals = [0, 1, 2, 3, 4, 5]
mu_vals = [0.1, 0.4, 0.8, 1.0, 0.6, 0.2]
# User lambda input
lam = float(input("Enter lambda value (0 to 1): "))
# Lambda cut
cut_x = [x for x, mu in zip(x_vals, mu_vals) if mu >= lam]
if cut_x:
    x_left = min(cut_x)
    x_right = max(cut_x)
    midpoint = (x_left + x_right) / 2
    print("\nLambda-cut elements:", cut_x)
    print("Lambda-cut interval:", [x_left, x_right])
    print("Defuzzified midpoint:", midpoint)
    # Plot fuzzy set
    plt.figure()
    plt.plot(x_vals, mu_vals, marker='o')
    plt.axhline(lam)
    # Highlight lambda-cut points
    for x in cut_x:
        idx = x_vals.index(x)
        plt.scatter(x, mu_vals[idx], s=100)
    plt.xlabel("x")
    plt.ylabel("Membership μ(x)")
    plt.title("Lambda-Cut Method on Discrete Fuzzy Set")
    plt.ylim(0, 1.1)
    plt.grid()
    plt.show()
else:
    print("No elements satisfy the lambda cut.")
