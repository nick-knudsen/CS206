import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

import os

from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        self.Prepare_To_Act()
        os.system("del brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timestep):
        for sensor in self.sensors.values():
            sensor.Get_Value(timestep)

    def Think(self):
        self.nn.Update()

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, robotId, timestep):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                jointName = bytes(jointName, 'utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(robotId, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        
        fitnessFile = open("fitness.txt", "w")
        fitnessFile.write(str(xCoordinateOfLinkZero))
        fitnessFile.close()
