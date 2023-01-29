import pyrosim.pyrosim as pyrosim
import numpy as np

pyrosim.Start_SDF("boxes.sdf")
[length, width, height] = [1,1,1]
[x,y,z] = [0,0,0.5]

for i in range(5):
    for j in range(5):
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+i,y+j,z+k] , size=np.multiply(0.9**k, [length, width, height]))

pyrosim.End()