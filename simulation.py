import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
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

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        # # simulation stepper
        for i in range(c.SIMULATION_STEPS):
            print(i)
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
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
            time.sleep(0.01)