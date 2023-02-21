import pybullet as p
import pybullet_data


class WORLD:
    def __init__(self):
        #p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # adding a floor
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")