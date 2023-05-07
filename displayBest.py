import numpy as np
import time
from solution import SOLUTION


for waveType in range(1, 4):
    for freq in [0.1, 0.2]:
        filename = "data/bestSolution_" + str(waveType) + "_" + str(freq) + ".npy"
        weights = np.load(filename)
        solution = SOLUTION(0, waveType, freq, False, weights)
        solution.Start_Simulation("GUI")
        time.sleep(10)