import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

class SOLUTION:

    def __init__(self, ID):
        self.weights = 2*np.random.rand(3,2)-1
        self.myID = ID

    def Set_ID(self, ID):
        self.myID = ID

    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        
        self.weights[row, col] = 2*random.random()-1

    def Evaluate(self, DirectOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system("start /B python simulate.py " + DirectOrGUI)
        
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        
        [length, width, height] = [1,1,1]
        [x,y,z] = [-3,3,0.5]
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
        
        pyrosim.End()

        return

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        [length, width, height] = [1,1,1]
        [x,y,z] = [1.5,0,1.5]
        pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length, width, height])
        
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()