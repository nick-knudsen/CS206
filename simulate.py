import pybullet as p   
import time

# create the GUI
physicsClient = p.connect(p.GUI)
# adding gravity
p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")
# simulation stepper
for i in range(5000):
    p.stepSimulation()
    time.sleep(0.01)
    print(i)
p.disconnect()