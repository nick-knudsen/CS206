import matplotlib.pyplot as plt
import numpy as np


labelKey = ["Sine", "Square", "Sawtooth"]
colors = 

for waveType in range(1,4):
    for freq in [0.1, 0.2]:
        filename = "data/fitnessVals_" + str(waveType) + "_" + str(freq) + ".npy"
        data = np.load(filename)
        data = np.mean(data, axis=0)
        label = "Mean Fitness for Robot with " + labelKey[waveType-1] + " CPG Neuron and Frequency " + str(freq)
        plt.plot(data, label = label, ) 

# targetAnglesFrontLeft = np.load("data/targetAnglesFrontLeft.npy")
# targetAnglesFrontRight = np.load("data/targetAnglesFrontRight.npy")
# targetAnglesBackLeft = np.load("data/targetAnglesBackLeft.npy")
# targetAnglesBackRight = np.load("data/targetAnglesBackRight.npy")

# plt.plot(targetAnglesFrontLeft, label = "Target Angle Front Left Leg")
# plt.plot(targetAnglesFrontRight, label = "Target Angle Front Right Leg")
# plt.plot(targetAnglesBackLeft, label = "Target Angle Back Left Leg")
# plt.plot(targetAnglesBackRight, label = "Target Angle Back Right Leg")

# cpgNeuronValuesSine = np.load("data/cpgNeuronVals_1.npy")
# cpgNeuronValuesSquare = np.load("data/cpgNeuronVals_2.npy")
# cpgNeuronValuesSaw = np.load("data/cpgNeuronVals_3.npy")

# plt.plot(cpgNeuronValuesSine, label = "Sinusoidal CPG Neuron Value")
# plt.plot(cpgNeuronValuesSquare, label = "Square Wave CPG Neuron Value")
# plt.plot(cpgNeuronValuesSaw, label = "Sawtooth Wave CPG Neuron Value")

plt.legend()
plt.show()