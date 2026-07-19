import numpy as np
import matplotlib.pyplot as plt
# =====================================================
# Triangular Membership Function (Stable Version)
# =====================================================
def trimf(x, a, b, c):
    x = np.array(x, dtype=float)
    y = np.zeros_like(x)
    # Left slope
    if b != a:
        y = np.where((a < x) & (x <= b), (x - a) / (b - a), y)
    # Right slope
    if c != b:
        y = np.where((b < x) & (x < c), (c - x) / (c - b), y)
    # Peak
    y = np.where(x == b, 1, y)
    return np.maximum(y, 0)
# =====================================================
# USER INPUT
# =====================================================
dirt = float(input("Enter Dirt Level (0-10): "))
load = float(input("Enter Load Size (0-10 kg): "))
# =====================================================
# UNIVERSE OF DISCOURSE
# =====================================================
dirt_range = np.linspace(0, 10, 200)
load_range = np.linspace(0, 10, 200)
wash_range = np.linspace(0, 60, 300)
# =====================================================
# MEMBERSHIP FUNCTIONS
# =====================================================
# Dirt
dirt_low = trimf(dirt_range, 0, 0, 5)
dirt_med = trimf(dirt_range, 2, 5, 8)
dirt_high = trimf(dirt_range, 5, 10, 10)
# Load
load_small = trimf(load_range, 0, 0, 5)
load_med = trimf(load_range, 2, 5, 8)
load_large = trimf(load_range, 5, 10, 10)
# Wash Time
wash_short = trimf(wash_range, 0, 0, 30)
wash_normal = trimf(wash_range, 20, 35, 50)
wash_long = trimf(wash_range, 40, 60, 60)
# =====================================================
# FUZZIFICATION (CRISP INPUT)
# =====================================================
d_low = float(trimf(dirt, 0, 0, 5))
d_med = float(trimf(dirt, 2, 5, 8))
d_high = float(trimf(dirt, 5, 10, 10))
l_small = float(trimf(load, 0, 0, 5))
l_med = float(trimf(load, 2, 5, 8))
l_large = float(trimf(load, 5, 10, 10))
# =====================================================
# RULE BASE (Mamdani - MIN operator)
# =====================================================
r1 = min(d_low, l_small) # Low dirt & Small load -> Short
r2 = min(d_low, l_large) # Low dirt & Large load -> Normal
r3 = min(d_med, l_med) # Medium dirt & Medium load -> Normal
r4 = min(d_high, l_small) # High dirt & Small load -> Normal
r5 = min(d_high, l_large) # High dirt & Large load -> Long
# =====================================================
# AGGREGATION
# =====================================================
aggregated = np.zeros_like(wash_range)
for i in range(len(wash_range)):
    aggregated[i] = max(
        min(r1, wash_short[i]),
        min(r2, wash_normal[i]),
        min(r3, wash_normal[i]),
        min(r4, wash_normal[i]),
        min(r5, wash_long[i])
    )
# =====================================================
# DEFUZZIFICATION (Centroid Method)
# =====================================================
numerator = np.sum(wash_range * aggregated)
denominator = np.sum(aggregated)
wash_time = numerator / denominator if denominator != 0 else 0
print("\nRecommended Wash Time:", round(wash_time, 2), "minutes")
# =====================================================
# ===================== PLOTS =========================
# =====================================================
# 1️⃣ Dirt Membership Plot
plt.figure()
plt.plot(dirt_range, dirt_low)
plt.plot(dirt_range, dirt_med)
plt.plot(dirt_range, dirt_high)
plt.title("Dirt Level Membership Functions")
plt.xlabel("Dirt Level")
plt.ylabel("Membership Value")
plt.show()
# 2️⃣ Load Membership Plot
plt.figure()
plt.plot(load_range, load_small)
plt.plot(load_range, load_med)
plt.plot(load_range, load_large)
plt.title("Load Size Membership Functions")
plt.xlabel("Load Size")
plt.ylabel("Membership Value")
plt.show()
# 3️⃣ Output Aggregated Plot
plt.figure()
plt.plot(wash_range, wash_short)
plt.plot(wash_range, wash_normal)
plt.plot(wash_range, wash_long)
plt.plot(wash_range, aggregated)
plt.title("Aggregated Wash Time Output")
plt.xlabel("Wash Time (minutes)")
plt.ylabel("Membership Value")
plt.show()
