import numpy as np
import pyrosim.pyrosim as pyrosim

import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.SIMULATION_STEPS)
    
    def Get_Value(self, timestep):
        self.values[timestep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        np.save("data/" + self.linkName + "SensorValues.npy", self.values)