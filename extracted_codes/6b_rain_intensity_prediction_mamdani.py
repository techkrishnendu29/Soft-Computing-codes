import numpy as np
import matplotlib.pyplot as plt
# -----------------------------
# Triangular Membership Function
# -----------------------------
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)
# -----------------------------
# Define Ranges
# -----------------------------
temperature = np.linspace(0, 40, 200)
humidity = np.linspace(0, 100, 200)
rain = np.linspace(0, 100, 200)
# -----------------------------
# Temperature Membership Functions
# -----------------------------
temp_low = triangular(temperature, 0, 10, 20)
temp_medium = triangular(temperature, 15, 22, 30)
temp_high = triangular(temperature, 25, 35, 40)
plt.figure()
plt.plot(temperature, temp_low)
plt.plot(temperature, temp_medium)
plt.plot(temperature, temp_high)
plt.title("Temperature Membership Functions")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.grid(True)
plt.show()
# -----------------------------
# Humidity Membership Functions
# -----------------------------
hum_low = triangular(humidity, 0, 30, 50)
hum_medium = triangular(humidity, 40, 60, 80)
hum_high = triangular(humidity, 70, 90, 100)
plt.figure()
plt.plot(humidity, hum_low)
plt.plot(humidity, hum_medium)
plt.plot(humidity, hum_high)
plt.title("Humidity Membership Functions")
plt.xlabel("Humidity (%)")
plt.ylabel("Membership Degree")
plt.grid(True)
plt.show()
# -----------------------------
# Example Crisp Inputs
# -----------------------------
temp_input = 18
hum_input = 85
# Fuzzification
t_low = triangular(temp_input, 0, 10, 20)
h_high = triangular(hum_input, 70, 90, 100)
# Rule:
# IF Temperature is Low AND Humidity is High → Heavy Rain
rule_strength = min(t_low, h_high)
# -----------------------------
# Rain Output Membership Functions
# -----------------------------
rain_no = triangular(rain, 0, 10, 30)
rain_light = triangular(rain, 20, 40, 60)
rain_heavy = triangular(rain, 50, 80, 100)
# Implication (clipping)
rain_output = np.minimum(rule_strength, rain_heavy)
plt.figure()
plt.plot(rain, rain_output)
plt.title("Aggregated Rain Output (Heavy Rain Rule)")
plt.xlabel("Rain Intensity")
plt.ylabel("Membership Degree")
plt.grid(True)
plt.show()
# -----------------------------
# Defuzzification (Centroid Method)
# -----------------------------
numerator = np.sum(rain * rain_output)
denominator = np.sum(rain_output) + 1e-6
crisp_rain = numerator / denominator
print("Predicted Rain Intensity:", crisp_rain)
