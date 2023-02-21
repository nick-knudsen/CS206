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
simulation.Run()
# SIMULATION_STEPS = c.SIMULATION_STEPS

# AMPLITUDE_FRONT = c.AMPLITUDE_FRONT
# FREQUENCY_FRONT = c.FREQUENCY_FRONT
# PHASE_OFFSET_FRONT = c.PHASE_OFFSET_FRONT

# AMPLITUDE_BACK = c.AMPLITUDE_BACK
# FREQUENCY_BACK = c.FREQUENCY_BACK
# PHASE_OFFSET_BACK = c.PHASE_OFFSET_BACK


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

# frontLegSensorValues = np.zeros(SIMULATION_STEPS)


# #np.save("data/targetAnglesFront.npy", targetAnglesFront)
# #np.save("data/targetAnglesBack.npy", targetAnglesBack)
# #exit()

# np.save("data/backLegSensorValues.npy", backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
