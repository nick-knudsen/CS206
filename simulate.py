from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
waveType = sys.argv[3]
freq = sys.argv[4]
simulation = SIMULATION(directOrGUI, solutionID, waveType, freq)
simulation.Run()
simulation.Get_Fitness()