import numpy as np
fuel_efficiency = np.array([25.0, 30.0, 28.0, 35.0])
average_efficiency = np.mean(fuel_efficiency)
model_1_efficiency = fuel_efficiency[0]
model_2_efficiency = fuel_efficiency[1]
percentage_improvement = ((model_2_efficiency - model_1_efficiency) / model_1_efficiency) * 100
print("Average fuel efficiency:", average_efficiency)
print("Percentage improvement in fuel efficiency from model 1 to model 2:", percentage_improvement)
