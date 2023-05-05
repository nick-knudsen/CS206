import matplotlib.pyplot as plt
import numpy as np

cpgNeuronValuesSine = np.load("data/cpgNeuronVals_1.npy")
cpgNeuronValuesSquare = np.load("data/cpgNeuronVals_2.npy")
cpgNeuronValuesSaw = np.load("data/cpgNeuronVals_3.npy")

# backLegSensorValues = np.load("data/backLegSensorValues.npy")
# frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

# targetAnglesFrontLeft = np.load("data/targetAnglesFrontLeft.npy")
# targetAnglesFrontRight = np.load("data/targetAnglesFrontRight.npy")
# targetAnglesBackLeft = np.load("data/targetAnglesBackLeft.npy")
# targetAnglesBackRight = np.load("data/targetAnglesBackRight.npy")

plt.plot(cpgNeuronValuesSine, label = "Sinusoidal CPG Neuron Value")
plt.plot(cpgNeuronValuesSquare, label = "Square Wave CPG Neuron Value")
plt.plot(cpgNeuronValuesSaw, label = "Sawtooth Wave CPG Neuron Value")

#plt.plot(backLegSensorValues, linewidth = 3, label = "Back Leg Sensor")
#plt.plot(frontLegSensorValues, label = "Front Leg Sensor")

# plt.plot(targetAnglesFrontLeft, label = "Target Angle Front Left Leg")
# plt.plot(targetAnglesFrontRight, label = "Target Angle Front Right Leg")
# plt.plot(targetAnglesBackLeft, label = "Target Angle Back Left Leg")
# plt.plot(targetAnglesBackRight, label = "Target Angle Back Right Leg")
plt.legend()
plt.show()