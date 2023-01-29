import pybullet as p
import pybullet_data
import time

# create the GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# adding gravity
p.setGravity(0,0,-9.8)
# adding a floor
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
# simulation stepper
for i in range(5000):
    p.stepSimulation()
    time.sleep(0.01)
    print(i)
p.disconnect()