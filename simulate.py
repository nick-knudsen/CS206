import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time

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
# simulation stepper
for i in range(5000):
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    p.stepSimulation()
    time.sleep(0.01)
    print(i)
p.disconnect()