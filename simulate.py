import pybullet as p   
import time

# create the GUI
physicsClient = p.connect(p.GUI)
# simulation stepper
for i in range(1000):
    p.stepSimulation()
    time.sleep(0.000001)
    print(i)
p.disconnect()