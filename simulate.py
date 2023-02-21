# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import pybullet_data
# import time
# import numpy as np
# from math import pi
# import random
# import constants as c
from simulation import SIMULATION


simulation = SIMULATION()

# SIMULATION_STEPS = c.SIMULATION_STEPS

# AMPLITUDE_FRONT = c.AMPLITUDE_FRONT
# FREQUENCY_FRONT = c.FREQUENCY_FRONT
# PHASE_OFFSET_FRONT = c.PHASE_OFFSET_FRONT

# AMPLITUDE_BACK = c.AMPLITUDE_BACK
# FREQUENCY_BACK = c.FREQUENCY_BACK
# PHASE_OFFSET_BACK = c.PHASE_OFFSET_BACK

# # create the GUI
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# # adding gravity
# p.setGravity(0,0,-9.8)
# # adding a floor
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = np.zeros(SIMULATION_STEPS)
# frontLegSensorValues = np.zeros(SIMULATION_STEPS)
# targetAnglesFront = AMPLITUDE_FRONT*np.sin(np.linspace(0+PHASE_OFFSET_FRONT,2*pi*FREQUENCY_FRONT+PHASE_OFFSET_FRONT, SIMULATION_STEPS))
# targetAnglesBack = AMPLITUDE_BACK*np.sin(np.linspace(0+PHASE_OFFSET_BACK,2*pi*FREQUENCY_BACK+PHASE_OFFSET_BACK, SIMULATION_STEPS))

# #np.save("data/targetAnglesFront.npy", targetAnglesFront)
# #np.save("data/targetAnglesBack.npy", targetAnglesBack)
# #exit()
# # simulation stepper
# for i in range(SIMULATION_STEPS):
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAnglesBack[i],
#         maxForce = 500
#     )
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAnglesFront[i],
#         maxForce = 500
#     )
#     p.stepSimulation()
#     time.sleep(0.01)
# np.save("data/backLegSensorValues.npy", backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# p.disconnect()