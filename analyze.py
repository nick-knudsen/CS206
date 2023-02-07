import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
plt.plot(backLegSensorValues, linewidth = 3, label = "Back Leg Sensor")
plt.plot(frontLegSensorValues, label = "Front Leg Sensor")
plt.legend()
plt.show()