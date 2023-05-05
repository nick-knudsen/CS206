from math import pi


SIMULATION_STEPS = 1000

AMPLITUDE_FRONT = pi/16
FREQUENCY_FRONT = 20
PHASE_OFFSET_FRONT = pi/16
AMPLITUDE_BACK = pi/16
FREQUENCY_BACK = 20
PHASE_OFFSET_BACK = 0

numberOfGenerations = 10
populationSize = 10

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.2

CPG_FREQUENCY = 0
CPG_WAVE_TYPE = 0

def setFreq(freq):
    global CPG_FREQUENCY
    CPG_FREQUENCY = freq
    
def setWaveType(waveType):
    global CPG_WAVE_TYPE # 1: Sinusoidal, 2: Square, 3: Sawtooth
    CPG_WAVE_TYPE = waveType