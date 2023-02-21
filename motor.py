import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
from math import pi


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE_FRONT
        self.frequency = c.FREQUENCY_FRONT
        self.offset = c.PHASE_OFFSET_FRONT

        self.motorValues = self.amplitude*np.sin(np.linspace(0+self.offset,2*pi*self.frequency+self.offset, c.SIMULATION_STEPS))
        
    def Set_Value(self):
        pass