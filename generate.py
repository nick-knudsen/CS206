import pyrosim.pyrosim as pyrosim
import numpy as np

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    [length, width, height] = [1,1,1]
    [x,y,z] = [-3,3,0.5]
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
    pyrosim.End()

    return


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    [length, width, height] = [1,1,1]
    [x,y,z] = [0,0,0.5]
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])
    pyrosim.End()

    return


Create_World()
Create_Robot()