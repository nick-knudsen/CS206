import pybullet as p


class WORLD:
    def __init__(self):
        # adding a floor
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")