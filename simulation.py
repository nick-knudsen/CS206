import pybullet as p
import pybullet_data
import time

from world import WORLD
from robot import ROBOT
import constants as c


class SIMULATION:
    def __init__(self):
        # create the GUI
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # adding gravity
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        # # simulation stepper
        for timestep in range(c.SIMULATION_STEPS):
            #print(timestep)

            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = b'Torso_BackLeg',
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAnglesBack[i],
            #     maxForce = 500
            # )
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = b'Torso_FrontLeg',
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAnglesFront[i],
            #     maxForce = 500
            # )
            p.stepSimulation()
            self.robot.Sense(timestep)
            time.sleep(0.01)
    
    def __del__(self):
        p.disconnect()