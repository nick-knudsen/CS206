import os
from parallelHillClimber import PARALLEL_HILLCLIMBER

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")
phc = PARALLEL_HILLCLIMBER()
phc.Evolve()
#phc.Show_Best()
