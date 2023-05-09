import pybullet as p
import pybullet_data
import time
import numpy as np

from world import WORLD
from robot import ROBOT
import constants as c


class SIMULATION:
    def __init__(self, directOrGUI, solutionID, waveType, freq):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        if directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # adding gravity
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

        self.waveType = waveType
        self.freq = freq


    def Run(self):
        # # simulation stepper
        for timestep in range(c.SIMULATION_STEPS):
            p.stepSimulation()
            self.robot.Sense(timestep)
            self.robot.Think(timestep, self.freq, self.waveType)
            self.robot.Act(self.robot.robotId, timestep)
            if self.directOrGUI == "GUI":
                time.sleep(0.001)
        footsteps = np.zeros((4, c.SIMULATION_STEPS))
        i = 0
        for sensor in self.robot.sensors.values():
            if sensor.linkName in ['BackLowerLeg','FrontLowerLeg','LeftLowerLeg','RightLowerLeg']:
                footsteps[i] = sensor.values
                i += 1
        np.save("data/sensorValues_" + self.waveType + "_" + self.freq + ".npy", footsteps)
        cpgVals = self.robot.cpgVals
        np.save("data/cpgNeuronVals_" + str(self.waveType), cpgVals)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()