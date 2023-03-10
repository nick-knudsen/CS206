import os
from hillclimber import HILLCLIMBER

for i in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")