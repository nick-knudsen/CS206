import os
from parallelHillClimber import PARALLEL_HILLCLIMBER
import constants as c

for waveType in range(1, 4):
    for freq in [0.1, 0.2]:
        c.setWaveType(waveType)
        c.setFreq(freq)
        phc = PARALLEL_HILLCLIMBER()
        phc.Evolve()
        phc.Show_Best()

