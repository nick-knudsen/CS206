import os
from parallelHillClimber import PARALLEL_HILLCLIMBER
import constants as c
import time

for waveType in range(1, 4):
    for freq in [0.1, 0.2]:
        phc = PARALLEL_HILLCLIMBER(waveType, freq)
        phc.Evolve()
        
        time.sleep(1)
        filename = "data/bestSolution_" + str(waveType) + "_" + str(freq)
        phc.Save_Best(filename)
