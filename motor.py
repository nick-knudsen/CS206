import numpy as np
import pybullet as p
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

        print(self.jointName)
        if self.jointName == b'Torso_BackLeg':
            print("test")
            self.frequency = 2*self.frequency
        self.motorValues = self.amplitude*np.sin(np.linspace(0+self.offset,2*pi*self.frequency+self.offset, c.SIMULATION_STEPS))
        
    def Set_Value(self, robotId, timestep):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[timestep],
            maxForce = 500
        )
    
    def Save_Values(self):
        np.save("data/targetAngles" + self.jointName + ".npy", self.motorValues)