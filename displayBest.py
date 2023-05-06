import numpy as np

from solution import SOLUTION


for waveType in range(1, 4):
    for freq in [0.1, 0.2]:
        filename = "bestSolution_" + str(waveType) + "_" + str(freq)
        weights = np.load(filename)
        solution = SOLUTION(0, waveType, freq, weights)
        solution.Start_Simulation("GUI")