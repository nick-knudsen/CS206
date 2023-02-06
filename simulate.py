import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy as np

# constants
SIMULATION_STEPS = 10000

# create the GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# adding gravity
p.setGravity(0,0,-9.8)
# adding a floor
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(SIMULATION_STEPS)
# simulation stepper
for i in range(SIMULATION_STEPS):
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    p.stepSimulation()
    time.sleep(0.01)
p.disconnect()