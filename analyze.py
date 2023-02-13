import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAnglesFront = np.load("data/targetAnglesFront.npy")
targetAnglesBack = np.load("data/targetAnglesBack.npy")

#plt.plot(backLegSensorValues, linewidth = 3, label = "Back Leg Sensor")
#plt.plot(frontLegSensorValues, label = "Front Leg Sensor")
plt.plot(targetAnglesFront, label = "Target Angle Front Leg")
plt.plot(targetAnglesBack, label = "Target Angle Back Leg")
plt.legend()
plt.show()