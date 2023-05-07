import pybullet as p
import time

class WORLD:
    def __init__(self):
        # adding a floor
        self.planeId = p.loadURDF("plane.urdf")
        worldLoaded = False
        while not worldLoaded:
            try:
                p.loadSDF("world.sdf")
            except:
                time.sleep(1)
            else:
                worldLoaded = True