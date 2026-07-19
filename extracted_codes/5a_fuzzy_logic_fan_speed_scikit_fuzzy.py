import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# 1 Define input and output universe
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')
print(temperature)
print(fan_speed)
# 2 Define membership functions
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['medium'] = fuzz.trimf(temperature.universe, [10, 20, 30])
temperature['high'] = fuzz.trimf(temperature.universe, [20, 40, 40])
fan_speed['slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 40])
fan_speed['moderate'] = fuzz.trimf(fan_speed.universe, [30, 50, 70])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [60, 100, 100])
# 3 Define rules
rule1 = ctrl.Rule(temperature['low'], fan_speed['slow'])
rule2 = ctrl.Rule(temperature['medium'], fan_speed['moderate'])
rule3 = ctrl.Rule(temperature['high'], fan_speed['fast'])
# 4 Create control system
fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)
# 5 Give input
fan_simulation.input['temperature'] = 28
# 6 Compute output
fan_simulation.compute()
# 7 Print result
print("Fan Speed:", fan_simulation.output['fan_speed'])
# 8 Visualize result
temperature.view()
fan_speed.view(sim=fan_simulation)
