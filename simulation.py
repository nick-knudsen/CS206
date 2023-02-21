import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        # create the GUI
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # adding gravity
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
